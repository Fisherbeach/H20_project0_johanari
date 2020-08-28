import calculator
def test_add():
    assert calculator.add(1,2)==3
def test_add2():
    assert calculator.add(-1,-2)==-3
def test_add3():
    assert calculator.add(0.999,1.01)==2.009