#Exercise 1-3
def add(x,y):
    return x+y

#Exercise 4.1
def factorial(x):
    if type(x)==float:
        raise Exception('Float is not valid')
    elif x<0:
        raise Exception('Factorial of negative not defined')
    elif x==0:
        return 1
    else:
        y=1
        for i in range(1,x+1):
            y*=i
        return y

#Exercise 4.2
def sin(x,N):
    if x<0:
        raise Exception(f'Sin of negative not defined')
    elif N<0 or type(N)==float:
        raise Exception(f'N can only be positive integer')
    else:
        y=0
        for i in range (N+1):
            y+=((-1)**i)*(x**(2*i+1)/factorial(2*i+1))
        return y

#Exercise 4.3
def division(x,y):
    if y==0:
        raise ZeroDivisionError('division by zero')
    elif type(x)==str or type(y)==str:
        raise TypeError('can only concatenate str (not "int") to str')
    else:
        return x/y

#Exercise 4.4 x in the power of y function
def x_power_y(x,y):
    if x==0 and y<0:
        raise ZeroDivisionError('division by zero')
    else:
        return x**y

#Exercise 4.5 absolute value
def absolute(x):
    if type(x)==str:
        raise ValueError('Only numbers allowed')
    else:
        x1=(x**2)**0.5
        if x1<0:
            raise Exception('Could not calculate |x|')
        else:
            return x1
            
         