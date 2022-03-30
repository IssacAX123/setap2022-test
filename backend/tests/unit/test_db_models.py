from decouple import config
from flask import Flask
from src.models import db

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"] = config("DB_URI")
db.init_app(app)
app.app_context().push()

from src.models.tables import User


def test_new_user_valid():
    args = {
        "firstname": "John",
        "lastname": "Smith",
        "email": "up207056@myport.ac.uk",
        "passwordenc": "password123*",
        "logintype": "email",
        "currentmpg": 24.1,
        "currentcityid": 2
    }
    new_user = User(**args)
    assert new_user.firstname == "John"
    assert new_user.lastname == "Smith"
    assert new_user.email == "up207056@myport.ac.uk"
    assert new_user.passwordenc == "password123*"
    assert new_user.logintype == "email"
    assert new_user.currentcityid == 2
    assert new_user.currentmpg == 24.1
