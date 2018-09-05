import random


def test_random():
    assert random.choice([1, 2]) == 2, "Random test failed"
