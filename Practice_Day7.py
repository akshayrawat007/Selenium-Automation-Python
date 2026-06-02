#Pytest
import time
import pytest

def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: critical path tests run on every build")
    config.addinivalue_line("markers", "regression: full regression suite")


def authenticate(username, password):
    valid_users = {"akshay123": "1234", "admin": "admin@99"}
    return "Login Successful" if valid_users.get(username) == password else "Invalid Credentials"


def withdraw(amount, balance: float = 113900.0):
    if amount <= 0:
        return "Invalid Amount"
    if amount > balance:
        return "Insufficient Balance"
    return "Transaction Successful"


def classify_number(n):
    return "even" if n % 2 == 0 else "odd"


def get_env_config(env):
    configs = {
         "staging":    {"base_url": "https://staging.example.com",  "timeout": 10},
        "production": {"base_url": "https://app.example.com",      "timeout": 5},
    }
    return configs.get(env, {})


@pytest.mark.smoke
def test_sanity_check():
    assert 10 == 10, "Sanity check failed"


def test_fstring_logging(capsys):
    name = "Akshay Rawat"
    message = f"Hello, {name}! Welcome to the framework."
    print(message)
    captured = capsys.readouterr()
    assert name in captured.out


@pytest.mark.smoke
@pytest.mark.parametrize("number, expected", [
    (4,  "even"),
    (7,  "odd"),
    (0,  "even"),
    (-3, "odd"),
])
def test_classify_number(number, expected):
    assert classify_number(number) == expected


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("username, password, expected", [
    ("akshay123", "1234",     "Login Successful"),
    ("akshay123", "wrong",    "Invalid Credentials"),
    ("admin",     "admin@99", "Login Successful"),
    ("",          "",         "Invalid Credentials"),
])
def test_login(username, password, expected):
    assert authenticate(username, password) == expected


@pytest.mark.skip(reason="BUG-id: OTP-based login flow not implemented yet")
def test_otp_login():
    assert authenticate("akshay123", "OTP:9982") == "Login Successful"

# change to "production" to run the skipped test
CURRENT_ENV = "staging"

@pytest.mark.regression
@pytest.mark.skipif(CURRENT_ENV != "production", reason="Runs only against production environment")
def test_production_timeout():
    config = get_env_config("production")
    assert config["timeout"] <= 5, "Production timeout exceeds SLA"


@pytest.mark.regression
@pytest.mark.skipif(CURRENT_ENV != "staging", reason="Runs only on staging environment")
def test_staging_base_url():
    config = get_env_config("staging")
    assert config["base_url"].startswith("https://staging"), "Unexpected staging URL"


@pytest.mark.xfail(reason="BUG-id: Insufficient-balance returns wrong message", strict=True)
def test_withdraw_insufficient_funds():
    assert withdraw(15_000) == "Insufficient Balance"

# Intentionally failing, but full suite will pass
@pytest.mark.xfail(reason="BUG-id: zero-amount raises unhandled exception", strict=False)
def test_withdraw_zero_amount():
    assert withdraw(0) == "Invalid Amount"


@pytest.mark.regression
def test_withdraw_valid():
    assert withdraw(5_000) == "Transaction Successful"


#pytest-xdist — parallel execution
# pytest -n 2
@pytest.mark.regression
@pytest.mark.parametrize("delay", [0.1, 0.1, 0.1, 0.1])
def test_parallel_simulation(delay):
    time.sleep(delay)
    assert delay > 0