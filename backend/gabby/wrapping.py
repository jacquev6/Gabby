from random import Random

from sqids import Sqids
from sqlalchemy.orm import DeclarativeBase, collections


# @todo Consider removing wrappers entierly: they might not be required with SQLAlchemy
# @todo Consider supporting client-provided hooks (per concrete class) for setattr and getattr in fastjsonapi to make the interface more flexible


class OrmWrapper:
    __slots__ = ["_wrapped"]

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def __getattr__(self, name):
        attr = getattr(self._wrapped, name)
        if isinstance(attr, DeclarativeBase):
            return wrap(attr)
        elif isinstance(attr, collections.InstrumentedList):
            return [wrap(item) for item in attr]
        else:
            return attr

    def __setattr__(self, name, value):
        if name == "_wrapped":
            super().__setattr__(name, value)
        else:
            try:
                attr = getattr(self._wrapped, name)
            except AttributeError:
                setattr(self._wrapped, name, value)
            else:
                if isinstance(attr, collections.InstrumentedList):
                    setattr(self._wrapped, name, [unwrap(item) for item in value])
                elif isinstance(value, OrmWrapper):
                    setattr(self._wrapped, name, unwrap(value))
                else:
                    setattr(self._wrapped, name, value)


class OrmWrapperWithStrIds(OrmWrapper):
    @property
    def id(self):
        return str(self._wrapped.id)


def make_sqids(name):
    random = Random(name)
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    random.shuffle(alphabet)
    sqids = Sqids(min_length=6, alphabet="".join(alphabet))
    # print(f"IDs of the first few {name}s:", " ".join(sqids.encode([i]) for i in range(1, 10)), flush=True)
    # @todo Return a wrapper that checks if the sqid is "canonical" (cf. https://sqids.org/faq#valid-ids)
    return sqids


# IDs of the first few exercises: wbqloc bylced jkrudc ufefwu orxbzq ahbwey vodhqn dymwin xnyegk
# IDs of the first few pdf_file_namings: tnahml wmyxrm yogtxq oexfhs bnqavf rhjojh pdbrtv uqodzk jgtoux
# IDs of the first few projects: xkopqm fryrbl ztmcex dillfm oqwpdb pbiqru handbn whkaxt tlfeqv
# IDs of the first few sections: eyjahd mknkny ajzqny fimocq nsbbfq rkqvdw qwozki tdchbv uygrig
# IDs of the first few textbooks: klxufv ojsbmy pkdksv alyral ixpuoz zsrfro deanft cpnkwb skhjfi
# IDs of the first few users: fvirvd ckylfa jahykn mrexcg pjxbru ywnpmi bhpuqj ztmkbr sgdyfj


def orm_wrapper_with_sqids(sqids):
    class Wrapper(OrmWrapper):
        @property
        def id(self):
            return sqids.encode([self._wrapped.id])

    return Wrapper


_wrappers = {}


def set_wrapper(type, base_wrapper):
    class Wrapper(base_wrapper):
        pass

    Wrapper.__name__ = type.__name__ + "Wrapper"

    _wrappers[type] = Wrapper


def get_wrapper(type):
    return _wrappers[type]


def wrap(o):
    if o is None:
        return None
    else:
        return get_wrapper(o.__class__)(o)


def unwrap(wrapper):
    return None if wrapper is None else wrapper._wrapped
