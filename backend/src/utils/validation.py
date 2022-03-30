class Validation:
    """Validation class with static validation methods"""

    @staticmethod
    def name_validation(name: str) -> object:
        """Validates name

        Args:
            name (str): name to validate

        Returns:
            object: error boolean (key='error') and error message (key='message')
        """
        if name == "" or not name.isalpha():
            return {"error": True, "message": "name is invalid"}
        else:
            return {"error": False, "message": ""}

    @staticmethod
    def email_validation(email: str) -> object:
        """Validates email

        Args:
            email (str): email to be validated

        Returns:
            object: error boolean (key='error') and error message (key='message')
        """
        if email == "" or "@" not in email or email[0] in [".", "-", "_"] or email[-1] in [".", "-", "_"]:
            return {"error": True, "message": "email is invalid"}
        for c in email:
            if not c.isalnum():
                if c not in [".", "-", "_", "@"]:
                    return {"error": True, "message": "email is invalid"}
        return {"error": False, "message": ""}

    @staticmethod
    def password_validation(password: str) -> object:
        """Validates password

        Args:
            password (str): password to be validated

        Returns:
            object: error boolean (key='error') and error message (key='message')
        """
        if password == "" or len(password) < 8:
            return {"error": True, "message": "password is invalid (too short)"}
        special_checker = [chr(x) for x in range(32, 65)] + [chr(x) for x in range(91, 97)] + \
                        [chr(x) for x in range(123, 128)]
        total_special_count = 0
        for c in password:
            if c in special_checker:
                total_special_count += 1
        if total_special_count < 2:
            return {"error": True, "message": "password is invalid (needs number or special character"}
        return {"error": False, "message": ""}
