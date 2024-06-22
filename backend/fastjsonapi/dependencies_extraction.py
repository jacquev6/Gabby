from typing import Annotated
import ast
import contextlib
import inspect
import typing
import unittest

from fastapi import Depends, Header
import fastapi.params


# class AstExplorationTestCase(unittest.TestCase):
#     def test(self):
#         print(ast.dump(ast.parse(textwrap.dedent("""\
#             class C:
#                 def __init__(self, *, a: annotations["a"], b: annotations["b"] = defaults["b"]):
#                     pass
#         """)), indent=4))


def extract_dependencies(target):
    signature = inspect.signature(target)

    annotations = {
        name: parameter.annotation
        for (name, parameter) in signature.parameters.items()
        if 
            isinstance(parameter.annotation, typing._AnnotatedAlias)
            and
            any(
                isinstance(metadata, (fastapi.params.Depends, fastapi.params.Param))
                for metadata in parameter.annotation.__metadata__
            )
    }

    defaults = {
        name: parameter.default
        for (name, parameter) in signature.parameters.items()
        if parameter.default is not inspect.Parameter.empty
    }

    from ast import Module, ClassDef, FunctionDef, Load, arguments, arg, Subscript, Name, Constant, Store, Assign, Dict, Attribute, Return, Call, keyword

    wrapper_ast = Module(
        body=[ClassDef(
            name="TargetWrapper",
            bases=[],
            keywords=[],
            body=[
                FunctionDef(
                    name="__init__",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[
                            arg(arg=name, annotation=Subscript(value=Name(id="annotations", ctx=Load()), slice=Constant(value=name), ctx=Load()))
                            for name in annotations
                        ],
                        kw_defaults=[
                            Subscript(value=Name(id="defaults", ctx=Load()), slice=Constant(value=name), ctx=Load()) if name in defaults else None
                            for name in annotations
                        ],
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Attribute(value=Name(id="self", ctx=Load()), attr="dependencies", ctx=Store())],
                            value=Dict(
                                keys=[Constant(value=name) for name in annotations],
                                values=[Name(id=name, ctx=Load()) for name in annotations],
                            )
                        ),
                    ],
                    decorator_list=[],
                    type_params=[],
                ),
                FunctionDef(name="__call__", args=arguments(posonlyargs=[], args=[arg(arg="self")], kwonlyargs=[], kw_defaults=[], kwarg=arg(arg="kwds"), defaults=[]), body=[Return(value=Call(func=Name(id="target", ctx=Load()), args=[], keywords=[keyword(value=Name(id="kwds", ctx=Load())), keyword(value=Attribute(value=Name(id="self", ctx=Load()), attr="dependencies", ctx=Load()))]))], decorator_list=[], type_params=[]),
            ],
            decorator_list=[],
            type_params=[],
        )],
        type_ignores=[],
    )
    ast.fix_missing_locations(wrapper_ast)

    # print(ast.unparse(wrapper_ast))

    # @todo Try and avoid exec, similarly to the "f = FunctionType(function_code, {})" part of https://stackoverflow.com/a/29927459/905845
    exec(compile(wrapper_ast, "<not_a_file>", "exec"), globals := dict(target=target, annotations=annotations, defaults=defaults))
    return globals["TargetWrapper"]


class ExtractDependenciesTestCase(unittest.TestCase):
    def test_no_parameters(self):
        def f():
            return 42

        self.assertEqual(extract_dependencies(f)()(), 42)

    def test_simple_parameter(self):
        def f(p: str):
            return p

        self.assertEqual(extract_dependencies(f)()(p="P"), "P")

    def test_defaulted_parameter(self):
        def f(p: str = "P"):
            return p

        self.assertEqual(extract_dependencies(f)()(), "P")

    def test_dependency(self):
        def f(d: Annotated[str, Depends()]):
            return d

        self.assertEqual(extract_dependencies(f)(d="D")(), "D")

    def test_header(self):
        def f(h: Annotated[str, Header()]):
            return h

        self.assertEqual(extract_dependencies(f)(h="H")(), "H")

    def test_defaulted_dependency(self):
        def f(d: Annotated[str, Depends()] = "D"):
            return d

        self.assertEqual(extract_dependencies(f)()(), "D")

    def test_defaulted_dependency_followed_by_non_defaulted_parameter(self):
        def f(*, d: Annotated[str, Depends()] = "D", nd: str):
            return (d, nd)

        self.assertEqual(extract_dependencies(f)()(nd="ND"), ("D", "ND"))

    def test_generator(self):
        def f():
            yield 42

        self.assertEqual(list(extract_dependencies(f)()()), [42])

    def test_context_manager(self):
        @contextlib.contextmanager
        def f():
            yield 42

        with extract_dependencies(f)()() as n:
            pass
        self.assertEqual(n, 42)


if __name__ == "__main__":
    unittest.main()
