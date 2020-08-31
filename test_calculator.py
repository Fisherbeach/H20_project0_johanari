import calculator
import math as mt
import pytest
#Exercise 1
def test_add(): #Checking if positive integers works
    assert calculator.add(1,2)==3 and calculator.add(-1,-2)==-3 

#Exercise 2
def test_add_float():    
    tol=1e-5 #Because of rounding errors, we need a tolerance
    assert abs(calculator.add(0.1,0.2)-0.3)<=tol

#Exercise 3
def test_add_string():
    string1="Hello "
    string2="World"
    assert calculator.add(string1,string2)=="Hello World"

#Exercise 4.1
def test_fac_pos_int():
    assert calculator.fac(1)==1 and calculator.fac(2)==2 and calculator.fac(5)==120
def test_fac_zero():
    assert calculator.fac(0)==1
def test_fac_neg_int():
    with pytest.raises(Exception) as e:
        assert calculator.fac(-1) and calculator.fac(-3)
    assert str(e.value)=='Factorial of negative not defined'
def test_fac_float():
    with pytest.raises(Exception) as f:
        assert calculator.fac(1/2) and calculator.fac(2.5)
    assert str(f.value)=='Float is not valid'
