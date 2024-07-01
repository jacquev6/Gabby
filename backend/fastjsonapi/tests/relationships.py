from __future__ import annotations
from contextlib import contextmanager
import dataclasses

from pydantic import BaseModel
from starlette import status

from ..testing import ApiTestCase, ItemsFactory


class TopModel(BaseModel):
    lefts: list[LeftModel] = []
    rights: list[RightModel] = []

class LeftModel(BaseModel):
    top: TopModel
    right_or_none: RightModel | None = None

class RightModel(BaseModel):
    top: TopModel
    left_or_none: LeftModel | None = None

class RelationshipsTestCase(ApiTestCase):
    class TopResource:
        singular_name = "top"
        plural_name = "tops"

        default_page_size = 2

        Model = TopModel

        @dataclasses.dataclass
        class Item:
            id: str

            lefts: list[RelationshipsTestCase.LeftResource.Item]
            rights: list[RelationshipsTestCase.RightResource.Item]

            saved: int = 0

        def __init__(self, factory):
            self.factory = factory

        def create_item(self, **kwds):
            return self.factory.create(self.Item, **kwds)

        def get_item(self, id):
            return self.factory.get(self.Item, id)

        def get_page(self, first_index, page_size):
            items = self.factory.get_all(self.Item)
            return (len(items), items[first_index:first_index + page_size])

        @contextmanager
        def save_item(self, item):
            yield
            item.saved += 1

    class LeftResource:
        singular_name = "left"
        plural_name = "lefts"

        default_page_size = 2

        Model = LeftModel

        @dataclasses.dataclass
        class Item:
            id: str

            top: RelationshipsTestCase.TopResource.Item
            right_or_none: RelationshipsTestCase.RightResource.Item | None

            saved: int = 0

        def __init__(self, factory):
            self.factory = factory

        def create_item(self, **kwds):
            return self.factory.create(self.Item, **kwds)

        def get_item(self, id):
            return self.factory.get(self.Item, id)

        @contextmanager
        def save_item(self, item):
            yield
            item.saved += 1

    class RightResource:
        singular_name = "right"
        plural_name = "rights"

        default_page_size = 2

        Model = RightModel

        @dataclasses.dataclass
        class Item:
            id: str

            top: RelationshipsTestCase.TopResource.Item
            left_or_none: RelationshipsTestCase.LeftResource.Item | None

            saved: int = 0

        def __init__(self, factory):
            self.factory = factory

        def get_item(self, id):
            return self.factory.get(self.Item, id)

    factory = ItemsFactory()
    # @todo Shuffle the resources to test their order doesn't matter
    resources = [TopResource(factory), LeftResource(factory), RightResource(factory)]

    def setUp(self):
        super().setUp()
        self.factory.clear()

    def test_create_top__minimal(self):
        response = self.post("http://server/tops", {
            "data": {
                "type": "topResource",
            },
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "top",
                "id": "1",
                "links": {"self": "http://server/tops/1"},
                "relationships": {
                    "lefts": {
                        "data": [],
                        "meta": {"count": 0},
                        # @todo Add links
                        # "links": {
                        #     "self": "http://server/tops/1/relationships/lefts",
                        #     "related": "http://server/tops/1/lefts"
                        # },
                    },
                    "rights": {
                        "data": [],
                        "meta": {"count": 0},
                    },
                },
            },
        })

        top = self.factory.get(self.TopResource.Item, "1")
        self.assertEqual(top.lefts, [])
        self.assertEqual(top.rights, [])

    def test_create_top__weirdly_empty(self):
        response = self.post("http://server/tops", {
            "data": {
                "type": "topResource",
                "relationships": {},
            },
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "top",
                "id": "1",
                "links": {"self": "http://server/tops/1"},
                "relationships": {
                    "lefts": {
                        "data": [],
                        "meta": {"count": 0},
                    },
                    "rights": {
                        "data": [],
                        "meta": {"count": 0},
                    },
                },
            },
        })

        top = self.factory.get(self.TopResource.Item, "1")
        self.assertEqual(top.lefts, [])
        self.assertEqual(top.rights, [])

    def test_create_top__explicitly_empty(self):
        response = self.post("http://server/tops", {
            "data": {
                "type": "topResource",
                "relationships": {
                    "lefts": {"data": []},
                    "rights": {"data": []},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "top",
                "id": "1",
                "links": {"self": "http://server/tops/1"},
                "relationships": {
                    "lefts": {
                        "data": [],
                        "meta": {"count": 0},
                    },
                    "rights": {
                        "data": [],
                        "meta": {"count": 0},
                    },
                },
            },
        })

        top = self.factory.get(self.TopResource.Item, "1")
        self.assertEqual(top.lefts, [])
        self.assertEqual(top.rights, [])

    def test_create_top__full(self):
        top = self.factory.create(self.TopResource.Item, lefts=[], rights=[])
        self.factory.create(self.LeftResource.Item, top=top, right_or_none=None)
        self.factory.create(self.LeftResource.Item, top=top, right_or_none=None)
        self.factory.create(self.RightResource.Item, top=top, left_or_none=None)
        self.factory.create(self.RightResource.Item, top=top, left_or_none=None)

        response = self.post("http://server/tops", {
            "data": {
                "type": "topResource",
                "relationships": {
                    "lefts": {"data": [{"type": "left", "id": "2"}, {"type": "left", "id": "3"}]},
                    "rights": {"data": [{"type": "right", "id": "4"}, {"type": "right", "id": "5"}]},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "top",
                "id": "6",
                "links": {"self": "http://server/tops/6"},
                "relationships": {
                    "lefts": {
                        "data": [{"type": "left", "id": "2"}, {"type": "left", "id": "3"}],
                        "meta": {"count": 2},
                    },
                    "rights": {
                        "data": [{"type": "right", "id": "4"}, {"type": "right", "id": "5"}],
                        "meta": {"count": 2},
                    },
                },
            },
        })

        top = self.factory.get(self.TopResource.Item, "6")
        self.assertEqual(top.lefts, [self.factory.get(self.LeftResource.Item, "2"), self.factory.get(self.LeftResource.Item, "3")])
        self.assertEqual(top.rights, [self.factory.get(self.RightResource.Item, "4"), self.factory.get(self.RightResource.Item, "5")])

    def test_create_left__minimal(self):
        self.factory.create(self.TopResource.Item, lefts=[], rights=[])

        response = self.post("http://server/lefts", {
            "data": {
                "type": "left",
                "relationships": {
                    "top": {"data": {"type": "top", "id": "1"}},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "left",
                "id": "2",
                "links": {"self": "http://server/lefts/2"},
                "relationships": {
                    "top": {"data": {"type": "top", "id": "1"}},
                    "rightOrNone": {"data": None},
                },
            },
        })

        left = self.factory.get(self.LeftResource.Item, "2")
        self.assertEqual(left.top, self.factory.get(self.TopResource.Item, "1"))
        self.assertEqual(left.right_or_none, None)

    def test_create_left__explicitly_none(self):
        self.factory.create(self.TopResource.Item, lefts=[], rights=[])

        response = self.post("http://server/lefts", {
            "data": {
                "type": "left",
                "relationships": {
                    "top": {"data": {"type": "top", "id": "1"}},
                    "rightOrNone": {"data": None},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "left",
                "id": "2",
                "links": {"self": "http://server/lefts/2"},
                "relationships": {
                    "top": {"data": {"type": "top", "id": "1"}},
                    "rightOrNone": {"data": None},
                },
            },
        })

        left = self.factory.get(self.LeftResource.Item, "2")
        self.assertEqual(left.top, self.factory.get(self.TopResource.Item, "1"))
        self.assertEqual(left.right_or_none, None)

    def test_create_left__full(self):
        top = self.factory.create(self.TopResource.Item, lefts=[], rights=[])
        self.factory.create(self.RightResource.Item, top=top, left_or_none=None)

        response = self.post("http://server/lefts", {
            "data": {
                "type": "left",
                "relationships": {
                    "top": {"data": {"type": "top", "id": "1"}},
                    "rightOrNone": {"data": {"type": "right", "id": "2"}},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "left",
                "id": "3",
                "links": {"self": "http://server/lefts/3"},
                "relationships": {
                    "top": {"data": {"type": "top", "id": "1"}},
                    "rightOrNone": {"data": {"type": "right", "id": "2"}},
                },
            },
        })

        left = self.factory.get(self.LeftResource.Item, "3")
        self.assertEqual(left.top, self.factory.get(self.TopResource.Item, "1"))
        self.assertEqual(left.right_or_none, self.factory.get(self.RightResource.Item, "2"))

    # @todo Add a test showing that "lid" can be used to create a resource related to itself

    def test_get_page__tops(self):
        top = self.factory.create(self.TopResource.Item, lefts=[], rights=[])
        for i in range(4):
            lefts = [self.factory.create(self.LeftResource.Item, top=top, right_or_none=None) for _ in range(i + 1)]
            rights = [self.factory.create(self.RightResource.Item, top=top, left_or_none=None) for _ in range(i + 1)]
            self.factory.create(self.TopResource.Item, lefts=lefts, rights=rights)

        response = self.get("http://server/tops?page[size]=3")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "top",
                    "id": "1",
                    "links": {"self": "http://server/tops/1"},
                    "relationships": {
                        "lefts": {
                            "data": [],
                            "meta": {"count": 0},
                        },
                        "rights": {
                            "data": [],
                            "meta": {"count": 0},
                        },
                    },
                },
                {
                    "type": "top",
                    "id": "4",
                    "links": {"self": "http://server/tops/4"},
                    "relationships": {
                        "lefts": {
                            "data": [{"id": "2", "type": "left"}],
                            "meta": {"count": 1},
                        },
                        "rights": {
                            "data": [{"id": "3", "type": "right"}],
                            "meta": {"count": 1},
                        },
                    },
                },
                {
                    "type": "top",
                    "id": "9",
                    "links": {"self": "http://server/tops/9"},
                    "relationships": {
                        "lefts": {
                            "data": [{"id": "5", "type": "left"}, {"id": "6", "type": "left"}],
                            "meta": {"count": 2},
                        },
                        "rights": {
                            "data": [{"id": "7", "type": "right"}, {"id": "8", "type": "right"}],
                            "meta": {"count": 2},
                        },
                    },
                },
            ],
            "links": {
                "first": "http://server/tops?page%5Bsize%5D=3&page%5Bnumber%5D=1",
                "last": "http://server/tops?page%5Bsize%5D=3&page%5Bnumber%5D=2",
                "next": "http://server/tops?page%5Bsize%5D=3&page%5Bnumber%5D=2",
                "prev": None,
            },
            "meta": {
                "pagination": {
                    "count": 5,
                    "page": 1,
                    "pages": 2,
                },
            },
        })

    def test_update_top__nothing(self):
        self.factory.create(self.TopResource.Item, lefts=[], rights=[])

        response = self.patch("http://server/tops/1", {
            "data": {
                "type": "topResource",
                "id": "1",
                # No "attributes", no "relationships"
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "top",
                "id": "1",
                "links": {"self": "http://server/tops/1"},
                "relationships": {
                    "lefts": {
                        "data": [],
                        "meta": {"count": 0},
                    },
                    "rights": {
                        "data": [],
                        "meta": {"count": 0},
                    },
                },
            },
        })

        top = self.factory.get(self.TopResource.Item, "1")
        self.assertEqual(top.lefts, [])
        self.assertEqual(top.rights, [])
        self.assertEqual(top.saved, 0)

    def test_update_top__one(self):
        top1 = self.factory.create(self.TopResource.Item, lefts=[], rights=[])
        right = self.factory.create(self.RightResource.Item, top=top1, left_or_none=None)
        top = self.factory.create(self.TopResource.Item, lefts=[], rights=[right])
        self.factory.create(self.LeftResource.Item, top=top, right_or_none=None)

        response = self.patch("http://server/tops/3", {
            "data": {
                "type": "topResource",
                "id": "3",
                "relationships": {
                    "lefts": {"data": [{"type": "left", "id": "4"}]},
                }
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "top",
                "id": "3",
                "links": {"self": "http://server/tops/3"},
                "relationships": {
                    "lefts": {
                        "data": [{"type": "left", "id": "4"}],
                        "meta": {"count": 1},
                    },
                    "rights": {
                        "data": [{"type": "right", "id": "2"}],
                        "meta": {"count": 1},
                    },
                },
            },
        })

        top = self.factory.get(self.TopResource.Item, "3")
        self.assertEqual(top.lefts, [self.factory.get(self.LeftResource.Item, "4")])
        self.assertEqual(top.rights, [self.factory.get(self.RightResource.Item, "2")])
        self.assertEqual(top.saved, 1)

    def test_update_top__full(self):
        top1 = self.factory.create(self.TopResource.Item, lefts=[], rights=[])
        left1 = self.factory.create(self.LeftResource.Item, top=top1, right_or_none=None)
        left2 = self.factory.create(self.LeftResource.Item, top=top1, right_or_none=None)
        top = self.factory.create(self.TopResource.Item, lefts=[left1, left2], rights=[])
        self.factory.create(self.RightResource.Item, top=top, left_or_none=None)
        self.factory.create(self.RightResource.Item, top=top, left_or_none=None)

        response = self.patch("http://server/tops/4", {
            "data": {
                "type": "topResource",
                "id": "4",
                "relationships": {
                    "lefts": {"data": []},
                    "rights": {"data": [{"type": "right", "id": "5"}, {"type": "right", "id": "6"}]},
                }
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "top",
                "id": "4",
                "links": {"self": "http://server/tops/4"},
                "relationships": {
                    "lefts": {
                        "data": [],
                        "meta": {"count": 0},
                    },
                    "rights": {
                        "data": [{"type": "right", "id": "5"}, {"type": "right", "id": "6"}],
                        "meta": {"count": 2},
                    },
                },
            },
        })

        top = self.factory.get(self.TopResource.Item, "4")
        self.assertEqual(top.lefts, [])
        self.assertEqual(top.rights, [self.factory.get(self.RightResource.Item, "5"), self.factory.get(self.RightResource.Item, "6")])
        self.assertEqual(top.saved, 1)

    def test_update_left__nothing(self):
        top = self.factory.create(self.TopResource.Item, lefts=[], rights=[])
        self.factory.create(self.LeftResource.Item, top=top, right_or_none=None)

        response = self.patch("http://server/lefts/2", {
            "data": {
                "type": "left",
                "id": "2",
                # No "attributes", no "relationships"
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "left",
                "id": "2",
                "links": {"self": "http://server/lefts/2"},
                "relationships": {
                    "top": {"data": {"type": "top", "id": "1"}},
                    "rightOrNone": {"data": None},
                },
            },
        })

        left = self.factory.get(self.LeftResource.Item, "2")
        self.assertEqual(left.top, top)
        self.assertEqual(left.right_or_none, None)
        self.assertEqual(left.saved, 0)

    def test_update_left__right_some(self):
        top = self.factory.create(self.TopResource.Item, lefts=[], rights=[])
        self.factory.create(self.LeftResource.Item, top=top, right_or_none=None)
        self.factory.create(self.RightResource.Item, top=top, left_or_none=None)

        response = self.patch("http://server/lefts/2", {
            "data": {
                "type": "left",
                "id": "2",
                "relationships": {
                    "rightOrNone": {"data": {"type": "right", "id": "3"}},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "left",
                "id": "2",
                "links": {"self": "http://server/lefts/2"},
                "relationships": {
                    "top": {"data": {"type": "top", "id": "1"}},
                    "rightOrNone": {"data": {"type": "right", "id": "3"}},
                },
            },
        })

        left = self.factory.get(self.LeftResource.Item, "2")
        self.assertEqual(left.top, self.factory.get(self.TopResource.Item, "1"))
        self.assertEqual(left.right_or_none, self.factory.get(self.RightResource.Item, "3"))
        self.assertEqual(left.saved, 1)

    def test_update_left__right_none(self):
        top = self.factory.create(self.TopResource.Item, lefts=[], rights=[])
        self.factory.create(self.LeftResource.Item, top=top, right_or_none=None)

        response = self.patch("http://server/lefts/2", {
            "data": {
                "type": "left",
                "id": "2",
                "relationships": {
                    "rightOrNone": {"data": None},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "left",
                "id": "2",
                "links": {"self": "http://server/lefts/2"},
                "relationships": {
                    "top": {"data": {"type": "top", "id": "1"}},
                    "rightOrNone": {"data": None},
                },
            },
        })

        left = self.factory.get(self.LeftResource.Item, "2")
        self.assertEqual(left.top, self.factory.get(self.TopResource.Item, "1"))
        self.assertEqual(left.right_or_none, None)
        self.assertEqual(left.saved, 1)

    def test_update_left__top(self):
        top = self.factory.create(self.TopResource.Item, lefts=[], rights=[])
        self.factory.create(self.LeftResource.Item, top=top, right_or_none=None)
        self.factory.create(self.TopResource.Item, lefts=[], rights=[])

        response = self.patch("http://server/lefts/2", {
            "data": {
                "type": "left",
                "id": "2",
                "relationships": {
                    "top": {"data": {"type": "top", "id": "3"}},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "left",
                "id": "2",
                "links": {"self": "http://server/lefts/2"},
                "relationships": {
                    "top": {"data": {"type": "top", "id": "3"}},
                    "rightOrNone": {"data": None},
                },
            },
        })

        left = self.factory.get(self.LeftResource.Item, "2")
        self.assertEqual(left.top, self.factory.get(self.TopResource.Item, "3"))
        self.assertEqual(left.right_or_none, None)
        self.assertEqual(left.saved, 1)

    def test_update_left__top_none(self):
        top = self.factory.create(self.TopResource.Item, lefts=[], rights=[])
        self.factory.create(self.LeftResource.Item, top=top, right_or_none=None)

        response = self.patch("http://server/lefts/2", {
            "data": {
                "type": "left",
                "id": "2",
                "relationships": {
                    "top": {"data": None},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY, response.json())
