from django.test import TestCase

from .router import parse_include


class ParseIncludeTests(TestCase):
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
