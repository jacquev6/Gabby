from __future__ import annotations
import dataclasses
from typing import Annotated
import itertools
import unittest

from fastapi import Depends, Query
import humps

from .testing import ApiTestCase
from mydantic import PydanticBase


def make_include_tuple(include_dict):
    return tuple((nested_name, make_include_tuple(nested_include_dict)) for (nested_name, nested_include_dict) in include_dict.items())


def parse_include(include: str | None):
    if include is None:
        return None
    elif include == "":
        return ()
    else:
        paths = [path.split(".") for path in include.split(",")]
        include_dict = {}
        for path in paths:
            current = include_dict
            for part in path:
                current = current.setdefault(part, {})
        return make_include_tuple(include_dict)


class ParseIncludeTestCase(unittest.TestCase):
    def test_none(self):
        self.assertEqual(parse_include(None), None)

    def test_empty_string(self):
        self.assertEqual(
            parse_include(""),
            (),
        )

    def test_single_item(self):
        self.assertEqual(
            parse_include("author"),
            (("author", ()),),
        )

    def test_multiple_items(self):
        self.assertEqual(
            parse_include("author,comments"),
            (("author", ()), ("comments", ())),
        )

    def test_nested_items(self):
        self.assertEqual(
            parse_include("comments.author.team.members"),
            (("comments", (("author", (("team", (("members", ()),)),)),)),),
        )

    def test_repeated_prefix(self):
        self.assertEqual(
            parse_include("comments.author.team.members.posts,comments.author.team.leader.comments"),
            (("comments", (("author", (("team", (("members", (("posts", ()),)), ("leader", (("comments", ()),)),)),)),)),),
        )


def include_dependable(include: Annotated[str, Query()] = None):
    return parse_include(include)


IncludeDependable = Annotated[dict | None, Depends(include_dependable)]


def make_included(root_resource, resources, urls, root_items, root_include):
    root_resource_name = root_resource.singular_name
    already_included = {(root_resource_name, root_item.id) for root_item in root_items}

    already_recursed = set()

    included = []

    def recurse(resource_name, resource, item, include):
        if (resource_name, item.id, include) not in already_recursed:
            already_recursed.add((resource_name, item.id, include))

            if (resource_name, item.id) not in already_included:
                already_included.add((resource_name, item.id))
                included.append(resource.make_item(resources, urls=urls, item=item))

            for (name, nested_include) in include:
                attribute = getattr(item, humps.decamelize(name))
                if attribute is None:
                    continue

                (is_list, nested_resource_names) = resource.output_relationships[name]
                if len(nested_resource_names) == 1:
                    nested_resource_name = nested_resource_names[0]
                else:
                    assert not is_list
                    nested_resource_name = root_resource.polymorphism[type(attribute)]
                for nested_item in attribute if is_list else [attribute]:
                    recurse(nested_resource_name, resources[nested_resource_name], nested_item, nested_include)

    for root_item in root_items:
        recurse(root_resource_name, root_resource, root_item, root_include)

    return sorted(included, key=lambda item: (item["type"], item["id"]))


class MakeIncludedTestCaseAlphaModel(PydanticBase):
    pass

class MakeIncludedTestCaseBravoModel(PydanticBase):
    pass

class MakeIncludedTestCaseNodeModel(PydanticBase):
    v: str
    parent: MakeIncludedTestCaseNodeModel | None = None
    children: list[MakeIncludedTestCaseNodeModel] = []
    polymorphic_scalar: MakeIncludedTestCaseAlphaModel | MakeIncludedTestCaseBravoModel | None = None

class MakeIncludedTestCase(ApiTestCase):
    class AlphaResource:
        singular_name = "alpha"
        plural_name = "alphas"

        default_page_size = 2

        Model = MakeIncludedTestCaseAlphaModel

        @dataclasses.dataclass
        class Item:
            id: str

        def get_item(self, id):
            return None

    class BravoResource:
        singular_name = "bravo"
        plural_name = "bravos"

        default_page_size = 2

        Model = MakeIncludedTestCaseBravoModel

        @dataclasses.dataclass
        class Item:
            id: str

        def get_item(self, id):
            return None

    class NodesResource:
        singular_name = "node"
        plural_name = "nodes"

        default_page_size = 2

        Model = MakeIncludedTestCaseNodeModel

        class Item:
            def __init__(self, id):
                self.id = str(id)
                self._parent = None
                self._children = []
                self.__v_got = False
                self.polymorphic_scalar = None
                self.polymorphic_list = []

            @property
            def v(self):
                assert not self.__v_got
                self.__v_got = True
                return f"v-{self.id}"

            @property
            def parent(self):
                return self._parent

            @property
            def children(self):
                return self._children

        def get_item(self, id):
            return None
        
        def get_page(self, first_index, page_size):
            return (2, [MakeIncludedTestCase._nodes["0"], MakeIncludedTestCase._nodes["1"]])

    resources = [NodesResource(), AlphaResource(), BravoResource()]
    polymorphism = {
        AlphaResource.Item: "alpha",
        BravoResource.Item: "bravo",
    }

    def do_test(self, include, expected_included):
        if include is None:
            query = ""
        else:
            query = f"?include={','.join(include)}"

        actual_included = self.get(f"/nodes{query}").json().get("included")

        if expected_included is None:
            self.assertIsNone(actual_included)
        else:
            self.assertEqual(
                [{"type": item["type"], "id": item["id"]} for item in actual_included],
                expected_included,
            )

    @classmethod
    def set_parent_child_relation(cls, parent_child_relation):
        nodes = {id: cls.NodesResource.Item(id) for id in {0, 1} | set(itertools.chain.from_iterable(parent_child_relation))}
        for (parent, child) in parent_child_relation:
            parent = nodes[parent]
            child = nodes[child]
            if child._parent is None:
                child._parent = parent
            parent._children.append(child)
        cls._nodes = {str(id): node for (id, node) in nodes.items()}

    @classmethod
    def set_polymorphic_scalars(cls, polymorphic_scalars):
        for (id, scalar) in polymorphic_scalars:
            cls._nodes[str(id)].polymorphic_scalar = scalar

    def test_no_include_from_lone_nodes(self):
        self.set_parent_child_relation([])
        self.do_test(
            None,
            None,
        )

    def test_include_nothing_from_lone_nodes(self):
        self.set_parent_child_relation([])
        self.do_test(
            [],
            [],
        )

    def test_include_parent_and_children_from_lone_node(self):
        self.set_parent_child_relation([])
        self.do_test(
            ["parent", "children"],
            [],
        )

    def test_include_children_from_parent(self):
        self.set_parent_child_relation([(0, 2), (0, 3), (1, 4)])
        self.do_test(
            ["children"],
            [
                {"type": "node", "id": "2"},
                {"type": "node", "id": "3"},
                {"type": "node", "id": "4"},
            ],
        )

    def test_include_parent_from_child(self):
        self.set_parent_child_relation([(2, 0), (3, 1)])
        self.do_test(
            ["parent"],
            [
                {"type": "node", "id": "2"},
                {"type": "node", "id": "3"},
            ],
        )

    def test_include_children_already_in_data(self):
        self.set_parent_child_relation([(0, 1)])
        self.do_test(
            ["children"],
            [],
        )

    def test_include_parent_already_in_data(self):
        self.set_parent_child_relation([(0, 1)])
        self.do_test(
            ["parent"],
            [],
        )

    def test_include_deep_children_from_diamond(self):
        self.set_parent_child_relation([(0, 2), (0, 3), (2, 4), (3, 4)])
        self.do_test(
            ["children.children"],
            [
                {"type": "node", "id": "2"},
                {"type": "node", "id": "3"},
                {"type": "node", "id": "4"},
            ],
        )

    def test_include_deep_children_from_diamond_already_in_data(self):
        self.set_parent_child_relation([(0, 2), (0, 3), (2, 1), (3, 1)])
        self.do_test(
            ["children.children"],
            [
                {"type": "node", "id": "2"},
                {"type": "node", "id": "3"},
            ],
        )

    def test_include_children_from_circular(self):
        self.set_parent_child_relation([(0, 2), (2, 0)])
        self.do_test(
            ["children"],
            [
                {"type": "node", "id": "2"},
            ],
        )

    def test_include_deep_children_from_circular(self):
        self.set_parent_child_relation([(0, 2), (2, 0)])
        self.do_test(
            ["children.children.children"],
            [
                {"type": "node", "id": "2"},
            ],
        )

    def test_include_deep_parent_from_circular(self):
        self.set_parent_child_relation([(0, 2), (2, 0)])
        self.do_test(
            ["parent.parent.parent"],
            [
                {"type": "node", "id": "2"},
            ],
        )

    def test_include_parent_from_circular(self):
        self.set_parent_child_relation([(0, 2), (2, 0)])
        self.do_test(
            ["parent"],
            [
                {"type": "node", "id": "2"},
            ],
        )

    def test_different_include_paths_for_same_node(self):
        #    2   7
        #   / \ /
        #  0   5
        #   \ / \
        #    3   6
        # First path: 0 --children--> 3 --parent--> 5
        # second path: 0 --parent--> 2 --children--> 5
        # then different relationships are included for 5: children and parent, proving that 5 must be recursed twice.

        self.set_parent_child_relation([(5, 3), (0, 3), (2, 0), (7, 5), (2, 5), (5, 6)])
        self.do_test(
            ["children.parent.children", "parent.children.parent"],
            [
                {"type": "node", "id": "2"},
                {"type": "node", "id": "3"},
                {"type": "node", "id": "5"},
                {"type": "node", "id": "6"},
                {"type": "node", "id": "7"},
            ],
        )

    def test_polymorphic_scalar(self):
        self.set_parent_child_relation([])
        self.set_polymorphic_scalars([(0, self.AlphaResource.Item("ALPHA"))])
        self.do_test(
            ["polymorphicScalar"],
            [
                {"type": "alpha", "id": "ALPHA"},
            ],
        )

    def test_children_polymorphic_scalar(self):
        self.set_parent_child_relation([(0, 2), (1, 3)])
        self.set_polymorphic_scalars([
            (1, self.AlphaResource.Item("ALPHA-1")),
            (2, self.AlphaResource.Item("ALPHA-2")),
            (3, self.BravoResource.Item("BRAVO-3")),
        ])
        self.do_test(
            ["children.polymorphicScalar"],
            [
                {"type": "alpha", "id": "ALPHA-2"},
                {"type": "bravo", "id": "BRAVO-3"},
                {"type": "node", "id": "2"},
                {"type": "node", "id": "3"},
            ],
        )
