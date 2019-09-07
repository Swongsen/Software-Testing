from a1 import bmi, retirement, shortestDistance, email

def test_bmi():
    # Test confirming http://extoxnet.orst.edu/faqs/dietcancer/web2/twohowto.html
    output = bmi('5\'3', '125')
    assert output == (22.7, 'Normal weight')

def test_retirement():
    output = retirement(25, '$100,000', '10%', '$1,000,000')
    assert output == (100)

def test_shortestDistance():
    # Testing the special triangle: 3, 4, 5
    output = shortestDistance(0, 0, 4, 3)
    assert output == 5

def test_email():
    output = email('email@email.com')
    assert output == 'Valid'
