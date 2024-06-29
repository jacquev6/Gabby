from typing import Annotated
import unittest

from fastapi import Depends, Query
import humps


def parse_include(include: str | None):
    if include is None:
        return None
    elif include == "":
        return {}
    else:
        paths = [path.split(".") for path in include.split(",")]
        return_value = {}
        for path in paths:
            current = return_value
            for part in path:
                current = current.setdefault(part, {})
        return return_value


class ParseIncludeTestCase(unittest.TestCase):
    def test_none(self):
        self.assertEqual(parse_include(None), None)

    def test_empty_string(self):
        self.assertEqual(parse_include(""), {})

    def test_single_item(self):
        self.assertEqual(parse_include("author"), {"author": {}})

    def test_multiple_items(self):
        self.assertEqual(parse_include("author,comments"), {"author": {}, "comments": {}})

    def test_nested_items(self):
        self.assertEqual(parse_include("comments.author.team.members"), {"comments": {"author": {"team": {"members": {}}}}})

    def test_repeated_prefix(self):
        self.assertEqual(
            parse_include("comments.author.team.members.posts,comments.author.team.leader.comments"),
            {"comments": {"author": {"team": {"members": {"posts": {}}, "leader": {"comments": {}}}}}},
        )


def include_dependable(include: Annotated[str, Query()] = None):
    return parse_include(include)


IncludeDependable = Annotated[dict | None, Depends(include_dependable)]


def make_included(root_resource, resources, urls, root_items, include):
    included = {}

    # @todo Add test showing we don't include the root items even if they appear in included relationships
    # @todo Add test showing we don't include the same item twice

    def recurse(resource, item, include):
        for (name, nested_include) in include.items():
            attr = getattr(item, humps.decamelize(name))
            (is_list, resource_names) = resource.output_relationships[name]
            if is_list:
                assert len(resource_names) == 1
                resource_name = resource_names[0]
                # @todo Add test showing that this variable ('nested_resource') cannot be named 'resource' (bug fixed using tests from Gabby, deserves test in fastjsonapi)
                nested_resource = resources[resource_name]
                for incl in attr:
                    included[(resource_name, incl.id)] = nested_resource.make_item(resources, urls=urls, item=incl)
                    recurse(nested_resource, incl, nested_include)
            elif attr is not None:
                if len(resource_names) == 1:
                    resource_name = resource_names[0]
                else:
                    resource_name = root_resource.polymorphism[type(attr)]
                # @todo Add test showing that this variable ('nested_resource') cannot be named 'resource' (bug fixed using tests from Gabby, deserves test in fastjsonapi)
                nested_resource = resources[resource_name]
                # @todo Add tests exercising this branch
                included[(resource_name, attr.id)] = nested_resource.make_item(resources, urls=urls, item=attr)
                recurse(nested_resource, attr, nested_include)

    for root_item in root_items:
        recurse(root_resource, root_item, include)

    return sorted(included.values(), key=lambda item: (item["type"], item["id"]))
