import pytest
from employee import Employee

@pytest.fixture
def employee():
    """A employee that available in all test function."""
    employee = Employee('quoc', 'phan')
    return employee

def test_give_default_raise(employee):
    """Test with default raise amount."""
    employee.give_raise()
    assert employee.salary == 5000

def test_give_custom_raise(employee):
    """Test with custom raise amount."""
    employee.give_raise(2000)
    assert employee.salary == 2000