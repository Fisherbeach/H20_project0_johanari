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
    assert calculator.fac(1)==1 and calculator.fac(2)==2 and calculator.fac(5)==120 #precalculated values
    assert calculator.fac(1)==mt.factorial(1) and calculator.fac(2)==mt.factorial(2)\
        and calculator.fac(5)==mt.factorial(5) #Comparing to factorial function in math library
def test_fac_zero():
    assert calculator.fac(0)==1 #Controlling that the factorial of 0 is equal to 1
def test_fac_neg_int():
    with pytest.raises(Exception) as e: #Controlling that Exception is raised for x<0
        assert calculator.fac(-1) and calculator.fac(-3)
    assert str(e.value)=='Factorial of negative not defined'
def test_fac_float():
    with pytest.raises(Exception) as f: #Controlling that Exeption is raised when x=float
        assert calculator.fac(1/2) and calculator.fac(2.5)
    assert str(f.value)=='Float is not valid' 

#Exercise 4.2
def test_sin_tol():
    tol=1e-6
    assert abs(calculator.sin(0,5)-mt.sin(0))<tol and abs(calculator.sin(0,5))<tol
    assert abs(calculator.sin(mt.pi/2,5)-mt.sin(mt.pi/2))<tol and abs(calculator.sin(mt.pi/2,5)-1)<tol
def test_sin_neg():
    with pytest.raises(Exception) as e:
        assert calculator.sin(-1,5) and calculator.sin(-mt.pi/2,5)
    assert str(e.value)=='Sin of negative not defined'
def test_sin_N():
    with pytest.raises(Exception) as f:
        assert calculator.sin(mt.pi/2,0.5)
    assert str(f.value)=='N can only be positive integer'

#Exercise 4.3
def test_division_values():
    tol=1e-6
    for arg, expected_output in [[(2,2),1],[(-2,2),-1],[(-3,-3),1],[(0.1,0.3),0.3333333]]:
        assert abs(calculator.divide(arg[0],arg[1])-expected_output)<tol
def test_division_zero():
    with pytest.raises(ZeroDivisionError) as e:
        assert calculator.division(1/0)
    assert str(f.value)=='Can not divide by zero'
def test_division_by_text():
    with pytest.raises(ValueError) as f:
        assert calculator.division('yes'/'no')
    assert str(f.value)=='x,y can only be floats or integers'    