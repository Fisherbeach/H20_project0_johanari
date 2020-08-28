import calculator
def test_add(): #Checking if positive integers works
    assert calculator.add(1,2)==3
def test_add2(): #Checking if negative integers works
    assert calculator.add(-1,-2)==-3 
def test_add3(): #Checking if float works
    tol=10e-5 #Because of rounding errors, we need a tolerance
    assert abs(calculator.add(0.1,0.2)-0.3)<=tol