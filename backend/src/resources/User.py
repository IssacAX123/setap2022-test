import logging
from flask_restful import Resource, request
import bcrypt

from src.models.tables import User, db
from src.resources.http_status_codes import *

from src.utils.validation import Validation


class NewUser(Resource):
    """NewUser class representing all endpoints related to new user
        Task class has the following methods:
        POST / .post() to register a new user.
        """

    def __init__(self):
        super().__init__()

    def post(self):
        """ endpoint = /api/v1/user/create

            Creates a new user by adding to database.
            Receives body containing 'first_name', 'last_name', 'email', 'login_method', 'current_city', 'current_mpg'
            and may also contain extra fields like 'password', 'oauth_id' depending on login_method.

            Returns:
                :obj:`flask.wrappers.Response`: a Response object containing empty json and status code
            """
        body = request.get_json()
        errors = self.validation(body)
        args = {
            "firstname": body["first_name"],
            "lastname": body["last_name"],
            "email": body["email"],
            "logintype": body["login_method"],
            "currentcityid": body["current_city"],
            "currentmpg": body["current_mpg"],
            "oauthid": None,
            "passwordenc": None
        }
        if body["login_method"] in ("google-oauth", "facebook-oauth"):
            args["oauthid"] = body["oauth_id"]
        elif body["login_method"] == "email":
            hashed_password = bcrypt.hashpw(body["password"].encode('utf-8'), bcrypt.gensalt())
            args["passwordenc"] = hashed_password.decode("utf-8")
        else:
            errors["messages "].insert(0, "login_method Invalid")
            errors["error"] = True

        if errors["error"]:
            return errors, CLIENT_ERROR
        else:
            new_user = User(**args)
            db.session.add(new_user)
            db.session.commit()
            errors["messages"] = ["Successfully added new user"]
            return errors, SUCCESS

    def validation(self, body: object, check_password: object = True) -> object:
        """ Validates user input for registration

            Runs the following validation methods: name_validation, email_validation, password_validation

            Args:
                body (object): request body in JSON
                check_password (boolean): default=True

            Returns:
                Object error boolean (key='error') and error messages list (key='messages')
            """
        name_validation = Validation.name_validation(body["first_name"])
        if not name_validation["error"]:
            name_validation = Validation.name_validation(body["last_name"])
        email_validation = Validation.email_validation(body["email"])
        if check_password:
            password_validation = Validation.password_validation(body["password"])
        else:
            password_validation = {"error": False, "message": ""}

        error_messages = []
        for test in [name_validation, email_validation, password_validation]:
            if test["error"]:
                error_messages.append(test["message"])
        if error_messages:
            return {"error": True, "messages": error_messages}
        else:
            return {"error": False, "messages": []}

