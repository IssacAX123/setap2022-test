from src.utils.validation import Validation


def test_name_validation_empty_string():
    error_object = Validation.name_validation("")
    assert error_object["error"] == True
    assert error_object["message"] == "name is invalid"


def test_name_validation_alphanumeric():
    error_object = Validation.name_validation("john78")
    assert error_object["error"] == True
    assert error_object["message"] == "name is invalid"


def test_name_validation_valid():
    error_object = Validation.name_validation("john")
    assert error_object["error"] == False
    assert error_object["message"] == ""


def test_email_validation_empty_string():
    error_object = Validation.email_validation("")
    assert error_object["error"] == True
    assert error_object["message"] == "email is invalid"


def test_email_validation_missing_at_symbol():
    error_object = Validation.email_validation("up203877myport.ac.uk")
    assert error_object["error"] == True
    assert error_object["message"] == "email is invalid"


def test_email_validation_invalid_char_at_start():
    error_object = Validation.email_validation("_up203877@myport.ac.uk")
    assert error_object["error"] == True
    assert error_object["message"] == "email is invalid"


def test_email_validation_invalid_char_at_end():
    error_object = Validation.email_validation("up203877@myport.ac.uk-")
    assert error_object["error"] == True
    assert error_object["message"] == "email is invalid"


def test_email_validation_invalid_char():
    error_object = Validation.email_validation("up203877(89)@myport.ac.uk")
    assert error_object["error"] == True
    assert error_object["message"] == "email is invalid"


def test_email_validation_valid():
    error_object = Validation.email_validation("up203877@myport.ac.uk")
    assert error_object["error"] == False
    assert error_object["message"] == ""


def test_password_validation_empty_string():
    error_object = Validation.password_validation("")
    assert error_object["error"] == True
    assert error_object["message"] == "password is invalid (too short)"


def test_password_validation_short_string():
    error_object = Validation.password_validation("pas1*")
    assert error_object["error"] == True
    assert error_object["message"] == "password is invalid (too short)"


def test_password_validation_no_special_chars_or_numbers():
    error_object = Validation.password_validation("passwordd")
    assert error_object["error"] == True
    assert error_object["message"] == "password is invalid (needs number or special character"


def test_password_validation_one_special_char_or_number():
    error_object = Validation.password_validation("password*")
    assert error_object["error"] == True
    assert error_object["message"] == "password is invalid (needs number or special character"


def test_password_validation_valid():
    error_object = Validation.password_validation("password1*")
    assert error_object["error"] == False
    assert error_object["message"] == ""
