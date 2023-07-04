from random import random

import pytest


CHANCE_TO_FAIL = 0.3  # 30%


@pytest.fixture()
def configgen(request):
    print("Testing for a fixture level exception")
    if flaky_boolean():
        raise Exception("In Fixture")
    else:
        return "HIIII"


@pytest.mark.flaky(max_runs=10, min_passes=1)
def test_1(request, configgen):
    print(configgen)


@pytest.mark.flaky(max_runs=10, min_passes=1)
def test_2(request):
    assert flaky_boolean()


@pytest.mark.flaky(max_runs=10, min_passes=1)
def test_3(request, configgen):
    print(configgen)


@pytest.mark.flaky(max_runs=10, min_passes=1)
def test_flaky_fixture(will_raise_sometimes):
    assert will_raise_sometimes is None


@pytest.mark.flaky(max_runs=10, min_passes=1)
def test_flaky_boolean():
    assert flaky_boolean() is True


@pytest.mark.flaky(max_runs=10, min_passes=1)
def test_flaky_raise():
    assert flaky_raise() is None


@pytest.fixture
def will_raise_sometimes():
    flaky_raise()


def flaky_boolean():
    return random() < CHANCE_TO_FAIL


def flaky_raise():
    if not flaky_boolean():
        raise Exception("Panic noooooow")
