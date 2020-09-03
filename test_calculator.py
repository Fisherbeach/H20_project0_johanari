import calculator
import math as mt
import pytest

#Exercise 1
@pytest.mark.parametrize('arg, expected_output', [[(1,2),3],[(-1,-2),-3]])
def test_add(arg, expected_output): #Checking if positive integers works
    assert calculator.add(arg[0],arg[1])==expected_output 

#Exercise 2
@pytest.mark.parametrize('arg, expected_output', [[(0.1,0.2),0.3],[(-0.1,-0.2),-0.3]])
def test_add_float(arg, expected_output):    
    tol=1e-6 #Because of rounding errors, we need a tolerance
    assert abs(calculator.add(arg[0],arg[1])-expected_output)<tol

#Exercise 3
def test_add_string():
    string1="Hello "
    string2="World"
    assert calculator.add(string1,string2)=="Hello World"

#Exercise 4.1
@pytest.mark.parametrize('x, o', [[1,1],[2,2],[5,120]])
def test_fac_pos_int(x, o):
    assert calculator.factorial(x)==o #precalculated values
    assert calculator.factorial(x)==mt.factorial(x) #Comparing to factorial function in math library

def test_fac_zero():
    assert calculator.factorial(0)==1 #Controlling that the factorial of 0 is equal to 1

@pytest.mark.parametrize('x',[-1,-3,-10])
def test_fac_neg_int(x):
    with pytest.raises(Exception) as e: #Controlling that Exception is raised for x<0
        assert calculator.factorial(x)
    assert str(e.value)=='Factorial of negative not defined'

@pytest.mark.parametrize('x',[0.5,2/3,10.1])    
def test_fac_float(x):
    with pytest.raises(Exception) as f: #Controlling that Exeption is raised when x=float
        assert calculator.factorial(1/2) and calculator.factorial(2.5)
    assert str(f.value)=='Float is not valid' 

#Exercise 4.2
@pytest.mark.parametrize('x, o',[[(0,7),0],[(mt.pi/2,7),1],[((5*mt.pi)/6,7), 0.5]])
def test_sin_tol(x,o):
    tol=1e-6
    assert abs(calculator.sin(x[0],x[1])-mt.sin(x[0]))<tol #Checking if it is sufficiently close to the math function
    assert abs(calculator.sin(x[0],x[1])-o)<tol #Checking if it is sufficiently close to the calculated value

@pytest.mark.parametrize('x',[[-1, 7],[-mt.pi/2, 7]])
def test_sin_neg(x):
    with pytest.raises(Exception) as e:
        assert calculator.sin(x[0],x[1])
    assert str(e.value)=='Sin of negative not defined'

def test_sin_N():
    with pytest.raises(Exception) as f:
        assert calculator.sin(mt.pi/2,0.5)
    assert str(f.value)=='N can only be positive integer'

#Exercise 4.3
@pytest.mark.parametrize('x, o', [[(2,2),1],[(-2,2),-1],[(-3,-3),1],[(0.1,0.3),0.3333333],[(0,1),0]])
def test_division_values(x, o):
    tol=1e-6
    assert abs(calculator.division(x[0],x[1])-o)<tol

def test_division_zero():
    with pytest.raises(ZeroDivisionError) as e:
        assert calculator.division(1,0)
    assert str(e.value)=='division by zero'

def test_division_by_text():
    with pytest.raises(TypeError) as f:
        assert calculator.division('yes'/'no')

#Exercise 4.4
@pytest.mark.parametrize('x, o', [[(1,1),1], [(1,0),1], [(-2,2),2]])
def test_x_power_y_value(x, o):
    assert calculator.x_power_y(x[0],x[1])==o

@pytest.mark.parametrize('x, o', [[(1,-1),1],[(2,-2),0.25],[(3,-1),0.333333]])
def test_x_power_y_negy(x, o):
    tol=1e-6
    assert abs(calculator.x_power_y(x[0],x[1])-o)<tol

def test_x_power_y_divzero():
    with pytest.raises(ZeroDivisionError) as e:
        assert calculator.x_power_y(0,-1)

#Exercise 5
def test_add_TypeError():
    with pytest.raises(TypeError) as e:
        assert calculator.add('yes',1)
    assert str(e.value)=='can only concatenate str (not "int") to str' #Also checking if the output is correct

def test_zerodivision():
    with pytest.raises(ZeroDivisionError) as f:
        assert calculator.division(1,0)
    assert str(f.value)=='division by zero'
