from application import shell_sort
import allure


def test_empty_array():
    """Testing sorting method using empty array"""
    array = []
    with allure.step("Asserting actual array with expected"):
        assert shell_sort(array) == []


def test_sorted_array():
    """Testing sorting method using sorted array"""
    array = [1, 2, 3, 4]
    with allure.step("Asserting actual array with expected"):
        assert shell_sort(array) == [1, 2, 3, 4]


def test_reversed_array():
    """Testing sorting method using reversed array"""
    array = [4, 3, 2, 1]
    with allure.step("Asserting actual array with expected"):
        assert shell_sort(array) == [1, 2, 3, 4]


def test_partly_sorted():
    """Testing sorting method using partly-sorted array"""
    array = [1, 2, 4, 3]
    with allure.step("Asserting actual array with expected"):
        assert shell_sort(array) == [1, 2, 3, 4]


def test_equal_values():
    """Testing sorting method using array with equal values"""
    array = [2, 2, 2, 2]
    with allure.step("Asserting actual array with expected"):
        assert shell_sort(array) == [2, 2, 2, 2]


def test_partly_equal_values():
    """Testing sorting method using array with partly-equal values"""
    array = [2, 2, 1, 1]
    with allure.step("Asserting actual array with expected"):
        assert shell_sort(array) == [1, 1, 2, 2]
