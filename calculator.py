#Exercise 1-3
def add(x,y):
    return x+y

#Exercise 4.1
def fac(x):
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