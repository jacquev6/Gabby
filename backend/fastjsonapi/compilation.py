# from __future__ import annotations  # This doesn't work because we're annotating with local types. So this code won't work on Python 4. OK.
from typing import Type
from urllib.parse import urlencode

import fastapi
import humps

from .annotations import Annotations
from .dependencies import extract_dependencies
from . import inclusion
from .models import Decider, make_create_input_model, make_output_models, make_update_input_model


def compile(resources, polymorphism: dict[Type, str]):
    decider = Decider({
        resource.Model: humps.camelize(resource.singular_name) for resource in resources
    })
    polymorphism = {
        key: humps.camelize(value)
        for (key, value) in polymorphism.items()
    }
    return {
        humps.camelize(resource.singular_name): CompiledResource(decider, polymorphism, resource)
        for resource in resources
    }


class CompiledResource:
    def __init__(self, decider, polymorphism, resource):
        self.polymorphism = polymorphism
        self._resource = resource

        assert humps.is_snakecase(resource.singular_name)
        self.singular_name = resource.singular_name
        self.singularName = humps.camelize(resource.singular_name)
        assert humps.is_snakecase(resource.plural_name)
        self.plural_name = resource.plural_name
        self.pluralName = humps.camelize(resource.plural_name)

        self.Model = resource.Model

        # @todo remove these 'else' branches: they were kept only to ease the transition to the new style
        if hasattr(resource, "create_item"):
            self.ItemCreator = extract_dependencies(resource.create_item)
        else:
            self.ItemCreator = getattr(resource, "ItemCreator", None)
        if hasattr(resource, "get_item"):
            self.ItemGetter = extract_dependencies(resource.get_item)
        else:
            self.ItemGetter = getattr(resource, "ItemGetter", None)
        if hasattr(resource, "get_page"):
            self.PageGetter = extract_dependencies(resource.get_page)
        else:
            self.PageGetter = getattr(resource, "PageGetter", None)
        if hasattr(resource, "save_item"):
            self.ItemSaver = extract_dependencies(resource.save_item)
        else:
            self.ItemSaver = getattr(resource, "ItemSaver", None)
        if hasattr(resource, "delete_item"):
            self.ItemDeleter = extract_dependencies(resource.delete_item)
        else:
            self.ItemDeleter = getattr(resource, "ItemDeleter", None)

        self.default_page_size = resource.default_page_size

        self.output_attributes = []
        self.output_relationships = {}
        self.create_input_relationships = {}
        self.update_input_relationships = {}
        for (name, info) in resource.Model.model_fields.items():
            name = humps.camelize(name)
            annotations = Annotations(info.metadata)

            if decider.is_mandatory_relationship(info.annotation):
                rel = (False, decider.get_polymorphic_names(info.annotation))
                if annotations.output:
                    self.output_relationships[name] = rel
                if annotations.create_input:
                    self.create_input_relationships[name] = rel
                if annotations.update_input:
                    self.update_input_relationships[name] = rel
            elif decider.is_optional_relationship(info.annotation):
                assert info.default is None
                rel = (False, decider.get_polymorphic_names(info.annotation))
                if annotations.output:
                    self.output_relationships[name] = rel
                if annotations.create_input:
                    self.create_input_relationships[name] = rel
                if annotations.update_input:
                    self.update_input_relationships[name] = rel
            elif decider.is_list_relationship(info.annotation):
                assert info.default == []
                rel = (True, decider.get_polymorphic_names(info.annotation))
                if annotations.output:
                    self.output_relationships[name] = rel
                if annotations.create_input:
                    self.create_input_relationships[name] = rel
                if annotations.update_input:
                    self.update_input_relationships[name] = rel
            else:
                if annotations.output:
                    self.output_attributes.append(name)

        self.CreateInputModel = make_create_input_model(self.singularName, resource.Model, decider)
        (self.ItemOutputModel, self.PageOutputModel) = make_output_models(self.singularName, resource.Model, decider)
        self.UpdateInputModel = make_update_input_model(self.singularName, resource.Model, decider)

    def make_item_response(self, resources, *, urls, item, include):
        return_value = {
            "data": self.make_item(resources, urls=urls, item=item),
        }
        if include is not None:
            return_value["included"] = self.make_included(resources, urls, [item], include)
        return return_value

    def make_page_response(self, resources, request: fastapi.Request, *, urls, items_count, page_number, page_size, items, include):
        pages_count = (items_count + 1) // page_size
        pagination = dict(count=items_count, page=page_number, pages=pages_count)

        base_url = urls.make(f"get_{self.plural_name}")
        def make_url_for_page(number):
            qs = dict(request.query_params)
            qs["page[number]"] = number
            if page_size != self.default_page_size:
                qs["page[size]"] = page_size
            return base_url + "?" + urlencode(qs)

        if page_number < pages_count:
            next = make_url_for_page(page_number + 1)
        else:
            next = None
        if page_number > 1:
            prev = make_url_for_page(page_number - 1)
        else:
            prev = None
        links = dict(
            first=make_url_for_page(1),
            last=make_url_for_page(pages_count),
            next=next,
            prev=prev,
        )

        return_value = {
            "data": [self.make_item(resources, urls=urls, item=item) for item in items],
            "links": links,
            "meta": dict(pagination=pagination),
        }
        if include is not None:
            return_value["included"] = self.make_included(resources, urls, items, include)
        return return_value

    def make_item(self, resources, *, urls, item):
        r = {
            "type": self.singularName,
            "id": item.id,
            "links": {"self": urls.make(f"get_{self.singular_name}", id=item.id)},
        }
        if self.output_attributes:
            attributes = {}
            for key in self.output_attributes:
                attr = getattr(item, humps.decamelize(key))
                attributes[key] = attr
            r["attributes"] = attributes
        if self.output_relationships:
            relationships = {}
            for (key, (is_list, resource_names)) in self.output_relationships.items():
                attr = getattr(item, humps.decamelize(key))
                if is_list:
                    assert len(resource_names) == 1
                    resource_name = resource_names[0]
                    data = [{"type": resource_name, "id": rel.id} for rel in attr]
                    relationship = {
                        "data": data,
                        "meta": {"count": len(data)},
                    }
                elif attr is None:
                    relationship = {"data": None}
                else:
                    if len(resource_names) == 1:
                        resource_name = resource_names[0]
                    else:
                        resource_name = self.polymorphism[type(attr)]
                    relationship = {"data": {"type": resource_name, "id": attr.id}}
                relationships[key] = relationship
            r["relationships"] = relationships
        return r

    make_included = inclusion.make_included
