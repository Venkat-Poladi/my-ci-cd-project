# These are automated tests for our app
# CodeBuild will run these automatically on every push

from app import hello

def test_hello_returns_string():
    result = hello()
    assert result == "Hello from my CI/CD pipeline!"

def test_hello_not_empty():
    result = hello()
    assert len(result) > 0
