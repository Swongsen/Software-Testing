from a1 import BMIfx

#this pytest bullshit is absolutely fucked
#need to figure out how to manually input user function input to a test method 
def test_normalweight_510_150(self):
    BMIfx.input = lambda: ''
    output = BMIfx(1.75, 67.5)
    assert output == '22'
