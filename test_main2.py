from main2 import get_weather, add, divide, UserManager
import pytest

def test_weather():
    assert get_weather(21).lower() == "hot"

def test_add():
    assert add(3,7) == 10
    assert add(-1,-1) == -2
    assert add(4,20) == 24


def test_divide():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(6,0)

# user_manager = UserManager()
@pytest.fixture()
def user_manager():
    return UserManager()

def test_add_user(user_manager):
    assert user_manager.add_user("john doe","john@example.com") == True
    assert user_manager.get_user("john doe") == "john@example.com"

def test_add_duplicate_user(user_manager):
    assert user_manager.add_user("john doe","john@example.com")
    with pytest.raises(ValueError):
        user_manager.add_user("john doe","another@example.com")


