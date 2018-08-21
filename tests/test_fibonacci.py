from fibonacci.fibonacci import fibonacci


def test_fibonacci_default():
    expected_result = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    actual_result = fibonacci()
    assert actual_result == expected_result, \
        "Fibonacci function without parameter: %s; expected was %s" % (actual_result, expected_result)


def test_fibonacci_twenty():
    expected_result = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    actual_result = fibonacci(20)
    assert actual_result == expected_result, \
        "Fibonacci function with parameter 20: %s; expected was %s" % (actual_result, expected_result)


def test_fibonacci_one():
    expected_result = 1
    actual_result = fibonacci(1)
    assert actual_result == expected_result,\
        "Fibonacci function with parameter 1: %s; expected was 1" % actual_result


def test_fibonacci_zero():
    expected_result = 0
    actual_result = fibonacci(0)
    assert actual_result == expected_result, \
        "Fibonacci function with parameter 0: %s; expected was 0" % actual_result


def test_fibonacci_negative():
    expected_result = 0
    actual_result = fibonacci(-999)
    assert actual_result == expected_result, \
        "Fibonacci function with negative parameter: %s; expected was 0" % actual_result
