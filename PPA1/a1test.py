from a1 import bmi, retirement, shortestDistance, isValidEmail

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

def test_retirement():
    # Testing a manually calculated answer
    assert retirement(25, '$100,000', '10%', '$1,000,000') == 100

    # Testing a goal that is achieved within 1 year
    assert retirement(25, '$1,000,000,000', '10%', '$1') == 26

def test_shortestDistance():
    # Testing the special triangle: 3, 4, 5
    assert shortestDistance(0, 0, 4, 3) == 5

    # Testing precision to 15 decimal points
    # Using special triangle: 1, sqrt(2), 3
    # Using sqrt(2) definition from https://apod.nasa.gov/htmltest/gifcity/sqrt2.1mil
    assert round(shortestDistance(0, 0, 1, 1), 15) == 1.414213562373095

def test_email():
    # email: some_string '@' domain

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
