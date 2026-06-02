import pytest

def test_demo():
    assert 10 == 10

def test_fstring():
    print()
    name = 'Akshay'
    print(f'Hello, {name}')

def is_even_or_odd(n):
    if n % 2 == 0:
        print(f"Number is even")
    else:
        print(f"Number is odd")

@pytest.mark.smoke
def test_odd_number():
    is_even_or_odd(9)


@pytest.mark.regression
def test_even_number():
    is_even_or_odd(2)

@pytest.mark.skip(reason="Functionality not developed yet")
def test_even5_number():
    is_even_or_odd(13   )

is_weekend = True

@pytest.mark.skipif(not is_weekend,reason="Not a weekend")
def test_oddeven_number():
    is_even_or_odd(5)


# Parameterization
def user_details(username,password):
    valid_username = "akshay123"
    valid_password = "1234"
    if username == valid_username and password == valid_password:
        return "Login Successful"
    return "Invalid Credentials"

@pytest.mark.smoke
@pytest.mark.parametrize('username,password,expected_result',[
    ("akshay", "122", "Invalid Credentials"),
    ("akshay123", "1234", "Login Successful"),
    ("akshay1", "12", "Invalid Credential"),]
)
def test_login(username,password,expected_result):
    result = user_details(username,password)
    assert result == expected_result


#xfail
def withdraw_balance(amount):
    current_balance = 12000
    if amount > current_balance:
        return "Transaction Failed"
    return "Transaction Successful"

@pytest.mark.xfail(reason="BUG-xyz: Incorrect message displayed for insufficient balance",strict=True)
def test_withdraw_balance():
    result = withdraw_balance(7000)
    assert result == "Insufficient Balance"









