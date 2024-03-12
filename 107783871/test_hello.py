from Hello import Hello

def test_default():
    assert Hello() == "Hello, World"

def test_argument():
    assert Hello("Gus") == "Hello, Gus"
