from app import add, greet

def test_add():
    assert add(4, 5) == 9
def test_greet():
    assert greet("Alex") == "Hello, Alex!"