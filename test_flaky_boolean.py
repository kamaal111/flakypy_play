from random import random

import pytest


def flaky_boolean():
    return random() < 0.6

@pytest.mark.flaky(max_runs=10, min_passes=1)
def test_flaky_boolean():
    assert flaky_boolean() is True
