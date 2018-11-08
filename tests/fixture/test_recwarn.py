import warnings

import pytest


def warn():
    warnings.warn('Deprecated function', DeprecationWarning)


def test_warn(recwarn):
    warn()
    assert len(recwarn) == 1
    w = recwarn.pop()
    assert w.category == DeprecationWarning


def test_warn2():
    with pytest.warns(None) as warnings:
        warn()

    assert len(warnings) == 1
    w = warnings.pop()
    assert w.category == DeprecationWarning
