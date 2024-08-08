import ast
import dataclasses
import textwrap
from typing import Annotated
import unittest

from fastapi import Depends, Query
from starlette import status
import humps

from .testing import ApiTestCase
from mydantic import PydanticBase
import mydantic


def make_filters_ast(fields):
    from ast import Module, FunctionDef, arguments, arg, Subscript, Name, Tuple, Load, Return, Call, keyword, Constant

    annotations = {}
    for (name, info) in fields.items():
        if info.annotation == str | None:
            type_ = "str"
        elif info.annotation == int | None:
            type_ = "int"
        else:
            assert False, info

        annotations[name] = Subscript(
            value=Name(id='Annotated', ctx=Load()),
            slice=Tuple(
                elts=[
                    Name(id=type_, ctx=Load()),
                    Call(
                        func=Name(id='Query', ctx=Load()),
                        args=[],
                        keywords=[keyword(arg='alias', value=Constant(value=f'filter[{humps.camelize(name)}]'))],
                    ),
                ],
                ctx=Load(),
            ),
            ctx=Load(),
        )

    module_ast = Module(
        body=[FunctionDef(
            name='filters',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg=name, annotation=annotation) for (name, annotation) in annotations.items()
                ],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[
                    Constant(value=None)
                    for name in fields.keys()
                ],
            ),
            body=[Return(value=Call(
                func=Name(id='filters_model', ctx=Load()),
                args=[],
                keywords=[
                    keyword(arg=name, value=Name(id=name, ctx=Load()))
                    for name in fields.keys()
                ],
            ))],
            decorator_list=[],
            type_params=[]
        )],
        type_ignores=[],
    )

    ast.fix_missing_locations(module_ast)

    return module_ast


class MakeFiltersAstTestCase(unittest.TestCase):
    def do_test(self, fields, expected):
        self.assertEqual(
            ast.unparse(make_filters_ast(fields)),
            textwrap.dedent(expected.lstrip("\n")).strip(),
        )

    # @todo Support mandatory string filters:
    # - with 'foo: str' instead of 'foo: str | None' in the filters_model
    # - without '= None' in the filter_code
    # @todo Support boolean filters:
    # - with 'foo: bool' in the filters_model
    # - that gets populated with True if the filter is present

    def test_empty(self):
        self.do_test(
            {},
            """
                def filters():
                    return filters_model()
            """,
        )

    def test_optional_str(self):
        self.do_test(
            {"s": mydantic.fields.FieldInfo(annotation=str | None)},
            """
                def filters(s: Annotated[str, Query(alias='filter[s]')]=None):
                    return filters_model(s=s)
            """,
        )

    def test_optional_int(self):
        self.do_test(
            {"i": mydantic.fields.FieldInfo(annotation=int | None)},
            """
                def filters(i: Annotated[int, Query(alias='filter[i]')]=None):
                    return filters_model(i=i)
            """,
        )

    def test_case_adaptation(self):
        self.do_test(
            {"identifier_with_several_words": mydantic.fields.FieldInfo(annotation=str | None)},
            """
                def filters(identifier_with_several_words: Annotated[str, Query(alias='filter[identifierWithSeveralWords]')]=None):
                    return filters_model(identifier_with_several_words=identifier_with_several_words)
            """,
        )

    def test_several(self):
        self.do_test(
            {
                "s1": mydantic.fields.FieldInfo(annotation=str | None),
                "s2": mydantic.fields.FieldInfo(annotation=str | None),
                "s3": mydantic.fields.FieldInfo(annotation=str | None),
            },
            """
                def filters(s1: Annotated[str, Query(alias='filter[s1]')]=None, s2: Annotated[str, Query(alias='filter[s2]')]=None, s3: Annotated[str, Query(alias='filter[s3]')]=None):
                    return filters_model(s1=s1, s2=s2, s3=s3)
            """,
        )


def make_filters(filters_model: type[PydanticBase]):
    filters_ast = make_filters_ast(filters_model.model_fields)

    # @todo Try and avoid exec, similarly to the "f = FunctionType(function_code, {})" part of https://stackoverflow.com/a/29927459/905845
    globals = {"filters_model": filters_model, "Query": Query, "Annotated": Annotated}
    exec(compile(filters_ast, "<not_a_file>", "exec"), globals)
    return Depends(globals["filters"])


class FilteringApiTestCase(ApiTestCase):
    class Resource:
        singular_name = "resource"
        plural_name = "resources"

        class Model(PydanticBase):
            filter_type: str
            filter_value: str

        @dataclasses.dataclass
        class Item:
            id: str

            filter_type: str
            filter_value: str

        default_page_size = 100

        def get_item(self, id: str):
            return None

        class Filters(PydanticBase):
            str: str | None
            an_int: int | None

        def get_page(self, filters: Annotated[Filters, make_filters(Filters)], first_index, page_size):
            # Filters usually remove items, but for this test they add items
            items = []
            if filters.str:
                assert isinstance(filters.str, str)
                items.append(self.Item(id=str(len(items)), filter_type="str", filter_value=filters.str))
            if filters.an_int:
                assert isinstance(filters.an_int, int)
                items.append(self.Item(id=str(len(items)), filter_type="int", filter_value=str(filters.an_int)))
            return (len(items), items)

    resources = [Resource()]

    def test_no_filter(self):
        response = self.get(f"http://server/resources")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
            ],
            "links": {
                "first": "http://server/resources?page%5Bnumber%5D=1",
                "last": "http://server/resources?page%5Bnumber%5D=0",  # @todo Fix: should be page%5Bnumber%5D=1
                "next": None,
                "prev": None,
            },
            "meta": {
                "pagination": {
                    "count": 0,
                    "page": 1,
                    "pages": 0,  # @todo Fix: should be 1
                },
            },
        })

    def test_str_filter(self):
        response = self.get(f"http://server/resources?filter[str]=STR")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "resource",
                    "id": "0",
                    "links": {
                        "self": "http://server/resources/0",
                    },
                    "attributes": {
                        "filterType": "str",
                        "filterValue": "STR",
                    },
                },
            ],
            "links": {
                "first": "http://server/resources?filter%5Bstr%5D=STR&page%5Bnumber%5D=1",
                "last": "http://server/resources?filter%5Bstr%5D=STR&page%5Bnumber%5D=0",  # @todo Fix: should be page%5Bnumber%5D=1
                "next": None,
                "prev": None,
            },
            "meta": {
                "pagination": {
                    "count": 1,
                    "page": 1,
                    "pages": 0,  # @todo Fix: should be 1
                },
            },
        })

    def test_int_filter(self):
        response = self.get(f"http://server/resources?filter[anInt]=42")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "resource",
                    "id": "0",
                    "links": {
                        "self": "http://server/resources/0",
                    },
                    "attributes": {
                        "filterType": "int",
                        "filterValue": "42",
                    },
                },
            ],
            "links": {
                "first": "http://server/resources?filter%5BanInt%5D=42&page%5Bnumber%5D=1",
                "last": "http://server/resources?filter%5BanInt%5D=42&page%5Bnumber%5D=0",  # @todo Fix: should be page%5Bnumber%5D=1
                "next": None,
                "prev": None,
            },
            "meta": {
                "pagination": {
                    "count": 1,
                    "page": 1,
                    "pages": 0,  # @todo Fix: should be 1
                },
            },
        })
