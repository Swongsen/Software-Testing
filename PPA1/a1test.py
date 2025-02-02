import pytest
from unittest.mock import Mock
from a1 import bmi, retirement, shortestDistance, isValidEmail, databaseCreation, priorEntries, databaseInsert

def test_databaseCreation(mocker):

    # Stub for databaseCreation
    def foo1(databaseCreation):
        databaseCreation(host='172.17.0.2', user='root', passwd='my-secret-pw')
    stub = mocker.stub(name='databaseCreation_stub')
    foo1(stub)
    # Asserts that the stub was called once with given parameters
    stub.assert_called_once_with(host='172.17.0.2', user='root', passwd='my-secret-pw')


    mock = Mock()
    # Using an assert_not_called mock to make sure that databaseCreation has not occured yet
    mock.databaseCreation.assert_not_called()
    mock.databaseCreation()
    # Using an assert_called() to make sure databaseCreation was called
    mock.databaseCreation.assert_called()
    # Using an assert_called_once mock to make sure databaseCreation was called only once
    mock.databaseCreation.assert_called_once()


def test_priorEntries(mocker):
    # Stub for priorEntries
    def foo2(priorEntries):
        priorEntries()
    stub = mocker.stub(name='priorEntries_stub')
    foo2(stub)
    stub.assert_called()

    mock = Mock()
    # Using an assert_not_called mock to make sure that priorEntries have not been called yet
    mock.priorEntries.assert_not_called()
    mock.priorEntries()
    # Using an assert_called() mock to make sure priorEntries was called
    mock.priorEntries.assert_called()
    # Using an assert_called_once() to make sure priorEntries was called only once
    mock.priorEntries.assert_called_once()

def test_databaseInsert(mocker):
    # Stub for database insert
    def foo3(databaseInsert):
        databaseInsert()
    stub = mocker.stub(name='databaseInsert_stub')
    foo3(stub)
    stub.assert_called()

    mock = Mock()
    # Using an assert_not_called mock to make sure that databaseInsert have not been called yet
    mock.databaseInsert.assert_not_called()
    mock.databaseInsert()
    # Using an assert_called() mock to make check if databaseInsert was called
    mock.databaseInsert.assert_called()
    # Using an assert_called_once() mock to make sure databaseInsert was called only once
    mock.databaseInsert.assert_called_once()

# Tests pytest's ability to check for an exception
def test_error():

    # Always raises a ValueError
    def error():
        raise ValueError('Hello')

    # Test should pass since error() raises an error
    with pytest.raises(ValueError):
        error()

def test_bmi():
    # Test confirming BMI calculation from:
    # http://extoxnet.orst.edu/faqs/dietcancer/web2/twohowto.html
    assert bmi('5\'3\"', '125') == (22.7, 'Normal weight')

    # Test Underweight
    assert bmi('5\'10\"', 50.5)[1] == 'Underweight'

    # Test Obese
    assert bmi('5\'0\"', 500)[1] == 'Obese'

    # Test Overweight
    assert bmi('5\'3\"', 155)[1] == 'Overweight'

    # ------- TESTS FOR INVALID INPUT ---------

    # Testing integer entered for height
    with pytest.raises(ValueError):
        bmi('34', '100')

    # Testing non-numeric value entered for height
    with pytest.raises(ValueError):
        bmi('A', '100')

    # Testing 2 single quotes
    with pytest.raises(ValueError):
        bmi('5\'\'10\"', '100')



def test_retirement():
    # Testing a manually calculated answer
    assert retirement(25, '$100,000', '10%', '$1,000,000') == 100

    # Testing a goal that is achieved within 1 year
    assert retirement(25, '$1,000,000,000', '10%', '$1') == 26

    # ------- TESTS FOR INVALID INPUT ---------

    # Test that a user can't be 100+ years old
    with pytest.raises(ValueError):
        retirement(100, '$1,000,000,000', '10%', '$1')

    # Test that ensures numeric inputs
    with pytest.raises(ValueError):
        retirement('A', 'B', 'C', 'D')

    # Tests for percent saved (can't be less than 0 or greater than 100)
    with pytest.raises(ValueError):
        retirement('50', '$50,000', '130%', '$100,000')
    with pytest.raises(ValueError):
        retirement('50', '$50,000', '-5%', '$100,000')

    # Test for salary (can't be less than 0)
    with pytest.raises(ValueError):
        retirement('50', '-$50,000', '5%', '$100,000')

def test_shortestDistance():

    # Testing the special triangle: 3, 4, 5
    assert shortestDistance(0, 0, 3, 4) == (0, 0, 3, 4, 5)

    # Testing precision to 15 decimal points
    # Using special triangle: 1, sqrt(2), 3
    # Using sqrt(2) definition from https://apod.nasa.gov/htmltest/gifcity/sqrt2.1mil
    assert shortestDistance(0, 0, 1, 1) == (0, 0, 1, 1, 1.4142135623730951)

    # ------- TESTS FOR INVALID INPUT ---------

    # Test for non-numeric input
    with pytest.raises(ValueError):
        shortestDistance('A', 'B', 'C', 'D')

def test_isValidEmail():
    # email: some_string '@' domain

    # Testing normal emails
    assert isValidEmail('student@ufl.edu') == True
    assert isValidEmail('account@email.com') == True
    assert isValidEmail('first.last@email.com') == True

    # Testing proper formatting
    # Needs @, and needs input for some_string and domain
    assert isValidEmail('test') == False
    assert isValidEmail('@email.com') == False
    assert isValidEmail('test@') == False

    # Testing that the email can be separated by periods
    assert isValidEmail('test.test.test@email.com') == True

    # Testing that no periods can start or end some_string
    assert isValidEmail('.test@email.com') == False
    assert isValidEmail('test.@email.com') == False

    # Testing that some_string can not have 2 periods in a row
    assert isValidEmail('te..st@email.com') == False

    # Testing that some_string starts with a non-numeric character
    assert isValidEmail('1test@email.com') == False

    # Test that some_string can contain certain special characters: !$%*+-=?^_{|}~
    assert isValidEmail('!$%*+-=?^_{|}~@email.com') == True

    # Test that some_string can NOT contain certain special characters: "(),:;<>@[\]'
    for char in '\"(),:;<>@[\\]\'':
        assert isValidEmail(char+'@email.com') == False

    # Test that domain is in the right format: x.y (Ex: abc.com, x=abc, y=com)
    # x.y.z..... is also valid
    assert isValidEmail('test@.aa') == False
    assert isValidEmail('test@aa.') == False
    assert isValidEmail('test@..') == False
    assert isValidEmail('test@x.y.z') == True

    # Testing for spaces in either the some_string or domain
    assert isValidEmail('te st@gmail.com') == False
    assert isValidEmail('test@gm ail.com') == False
