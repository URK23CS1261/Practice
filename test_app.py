from app import add, greet

def test_add():
    assert add(1, 4) == 5
def test_greet():
    assert greet("Alex") == "Hello, Alex!"