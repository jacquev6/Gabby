from typing import Annotated
import unittest

from fastapi import Depends, Query


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
