"""module to get funtionality for testing modules"""
import pytest
from user_reg import UserValidation
@pytest.fixture
def user():
    """fixture for pytest to create a user object"""
    return UserValidation()

def test_validate_password_should_return_success(user):
    """method for password success validation"""
    assert user.password is None
    user.validate_password("Nutankumar123")
    assert user.password == "Nutankumar123"

def test_validate_firstname_should_return_success(user):
    """method for firstname success validation"""
    assert user.first_name is None
    user.validate_fname("Nutan")
    assert user.first_name == "Nutan"

def test_validate_lastname_should_return_success(user):
    """method for lastname success validation"""
    assert user.last_name is None
    user.validate_lname("Kumar")
    assert user.last_name == "Kumar"

def test_validate_phone_should_return_success(user):
    """method for phone number success validation"""
    assert user.phone is None
    user.validate_phone("91 7281875750")
    assert user.phone == "91 7281875750"

def test_validate_email_should_return_success(user):
    """method for email success validation"""
    assert user.email is None
    user.validate_email("nk6583@srmist.edu.in")
    assert user.email == "nk6583@srmist.edu.in"


def test_validate_password_should_return_value_error(user):
    """method for password error validation"""
    assert user.password is None
    with pytest.raises(ValueError):
        user.validate_password("Nutank")

def test_validate_email_should_return_value_error(user):
    """method for email error validation"""
    assert user.email is None
    with pytest.raises(ValueError):
        user.validate_email("kumarnutan204")

def test_validate_fname_should_return_value_error(user):
    """method for firstname error validation"""
    assert user.first_name is None
    with pytest.raises(ValueError):
        user.validate_fname("nutan")

def test_validate_lname_should_return_value_error(user):
    """method for lastname error validation"""
    assert user.last_name is None
    with pytest.raises(ValueError):
        user.validate_lname("kumar")

def test_validate_phone_number_should_return_value_error(user):
    """method for phone number error validation"""
    assert user.phone is None
    with pytest.raises(ValueError):
        user.validate_phone("85452585")
