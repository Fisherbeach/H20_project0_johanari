import calculator
def test_add(): #Checking if positive integers works
    assert calculator.add(1,2)==3
    assert calculator.add(-1,-2)==-3 
def test_add_float():    
    tol=10e-5 #Because of rounding errors, we need a tolerance
    assert abs(calculator.add(0.1,0.2)-0.3)<=tol
def test_add_string():
    string1="Hello "
    string2="World"
    assert calculator.add(string1,string2)=="Hello World"