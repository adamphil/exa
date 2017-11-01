# -*- coding: utf-8 -*-
# Copyright (c) 2015-2017, Exa Analytics Development Team
# Distributed under the terms of the Apache License 2.0
"""
Tests for Strong Typing
########################
See :mod:`~exa.typed`
"""
import six
import pytest
from itertools import product
from exa.typed import Typed, typed, TypedClass, TypedMeta, yield_typed


@typed
class Simple1(object):
    foo = Typed(int)

    def __init__(self, foo):
        self.foo = foo


class Simple2(TypedClass):
    foo = Typed(int)

    def __init__(self, foo):
        self.foo = foo


class Simple3(six.with_metaclass(TypedMeta, Simple1)):
    pass


# params makes it so we test all the classes listed
params = list(product([Simple1, Simple2, Simple3],
                      [42, 42.0]))
@pytest.fixture(scope="session", params=params)
def simple(request):
    cls = request.param[0]
    arg = request.param[1]
    return cls(arg)


def test_simple(simple):
    """Test trivial typing."""
    assert isinstance(simple.foo, int)
    with pytest.raises(TypeError):
        simple.foo = "forty two"
    del simple._foo
    assert simple.foo is None
    assert len(list(yield_typed(simple))) == 1


# Complex example
def pre_set(obj):
    obj.pre_set_called = True


def pre_del(obj):
    obj.pre_del_called = True


class Complete(TypedClass):
    """Test advanced usage."""
    foo = Typed(int, doc="Test documentation", autoconv=False, allow_none=False,
                pre_set=pre_set, pre_get="pre_get", pre_del=pre_del, post_del="post_del")

    def pre_get(self):
        self.pre_get_called = True

    def post_del(self):
        self.post_del_called = True

    def __init__(self):
        self.pre_del_called = False
        self.post_del_called = False
        self.pre_del_called = False
        self.pre_get_called = False
        self.pre_set_called = False


@pytest.fixture(scope="session")
def cmplx():
    return Complete()


def test_complex(cmplx):
    """Test auxiliary options of Typed attributes."""
    assert cmplx.pre_set_called == False
    assert cmplx.pre_get_called == False
    none = cmplx.foo
    assert none is None
    assert cmplx.pre_get_called == True
    assert cmplx.pre_set_called == False
    cmplx.foo = 42
    assert cmplx.pre_set_called == True
    assert len(list(yield_typed(cmplx))) == 1
    with pytest.raises(TypeError):
        cmplx.foo = 42.0
    assert cmplx.pre_del_called == False
    assert cmplx.post_del_called == False
    del cmplx.foo
    assert cmplx.pre_del_called == True
    assert cmplx.post_del_called == True
    assert "Test documentation" in cmplx.__class__.foo.__doc__


class Simple4(TypedClass):
    _setters = ("_set", )
    foo = Typed(int)

    def _set_foo(self):
        self.foo = 42


@pytest.fixture(scope="session")
def auto():
    return Simple4()


def test_auto(auto):
    """Test automatic setting."""
    assert auto.foo == 42
