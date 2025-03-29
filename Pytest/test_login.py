def test_1():
    x=10
    y=10
    assert x==y

def test_2():
    name = "Selenium"
    Title="I am a Selenium Automation Tester"
    assert name in Title

def test_3():
    name="Jenkins"
    Title="Jenkin is a Continuous Integration"
    assert name in Title , "Title does not match"