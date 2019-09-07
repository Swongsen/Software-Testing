from a1 import bmi, retirement, shortestDistance, email

def test_bmi():
    # Test confirming BMI calculation from:
    # http://extoxnet.orst.edu/faqs/dietcancer/web2/twohowto.html
    assert bmi('5\'3', '125') == (22.7, 'Normal weight')

def test_retirement():
    assert retirement(25, '$100,000', '10%', '$1,000,000') == 100

def test_shortestDistance():
    # Testing the special triangle: 3, 4, 5
    assert shortestDistance(0, 0, 4, 3) == 5

def test_email():
    # email: some_string '@' domain

    # Testing proper formatting
    # Needs @, and needs input for some_string and domain
    assert email('test') == 'Invalid'
    assert email('@email.com') == 'Invalid'
    assert email('test@') == 'Invalid'

    # Testing that the email can be separated by periods
    assert email('test.test.test@email.com') == 'Valid'

    # Testing that no periods can start or end some_string
    assert email('.test@email.com') == 'Invalid'
    assert email('test.@email.com') == 'Invalid'

    # Testing that some_string can not have 2 periods in a row
    assert email('te..st@email.com') == 'Invalid'

    # Testing that some_string starts with a non-numeric character
    assert email('1test@email.com') == 'Invalid'

    # Test that some_string can contain certain special characters: !$%*+-=?^_{|}~
    assert email('!$%*+-=?^_{|}~@email.com') == 'Valid'

    # Test that some_string can NOT contain certain special characters: "(),:;<>@[\]'
    for char in '\"(),:;<>@[\\]\'':
        assert email(char+'@email.com') == 'Invalid'
