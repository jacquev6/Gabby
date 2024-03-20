from django.db import models


class DjangoOrmWrapper:
    __slots__ = ["_wrapped"]

    def __init__(self, wrapped):
        self._wrapped = wrapped

    @property
    def id(self):
        return str(self._wrapped.id)

    def save(self):
        self._wrapped.save()

    def delete(self):
        self._wrapped.delete()

    def __getattr__(self, name):
        attr = getattr(self._wrapped, name)
        if attr.__class__.__name__ == "RelatedManager":
            return [DjangoOrmWrapper(item) for item in attr.all()]
        elif isinstance(attr, models.Model):
            return DjangoOrmWrapper(attr)
        else:
            return attr

    def __setattr__(self, name, value):
        if name == "_wrapped":
            super().__setattr__(name, value)
        else:
            attr = getattr(self._wrapped, name)
            if attr.__class__.__name__ == "RelatedManager":
                attr.set([unwrap(v) for v in value])
            elif isinstance(attr, models.Model):
                setattr(self._wrapped, name, unwrap(value))
            else:
                setattr(self._wrapped, name, value)


def unwrap(wrapper):
    return None if wrapper is None else wrapper._wrapped
