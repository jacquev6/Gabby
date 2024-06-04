from django.db import models


class OrmWrapper:
    __slots__ = ["_wrapped"]

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def __getattr__(self, name):
        attr = getattr(self._wrapped, name)
        if attr.__class__.__name__ == "RelatedManager":
            return [wrap(item) for item in attr.all()]
        elif isinstance(attr, models.Model):
            return wrap(attr)
        else:
            return attr

    def __setattr__(self, name, value):
        if name == "_wrapped":
            super().__setattr__(name, value)
        else:
            attr = getattr(self._wrapped, name)
            if attr.__class__.__name__ == "RelatedManager":
                attr.set([unwrap(v) for v in value])
            elif isinstance(value, OrmWrapper):
                setattr(self._wrapped, name, unwrap(value))
            else:
                setattr(self._wrapped, name, value)


class OrmWrapperWithStrIds(OrmWrapper):
    @property
    def id(self):
        return str(self._wrapped.id)


_wrappers = {}

def set_wrapper(type, base_wrapper):
    class Wrapper(base_wrapper):
        pass

    Wrapper.__name__ = type.__name__ + "Wrapper"

    _wrappers[type] = Wrapper


def get_wrapper(type):
    return _wrappers[type]


def wrap(o):
    assert o is not None
    return get_wrapper(o.__class__)(o)


def unwrap(wrapper):
    return None if wrapper is None else wrapper._wrapped
