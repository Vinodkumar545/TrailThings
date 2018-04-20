import pytest


@pytest.allure.step
def make_test_data_foo():
    print("make_test_data_foo")


def test_foo():
    assert make_test_data_foo() is not None


@pytest.allure.step('make_some_data_foo')
def make_some_data_bar():
    print("make_some_data_bar")


def test_bar():
    assert make_some_data_bar() is not None