import bcrypt
from flask_restful import Api
from src.app import create_app


def create_api():
    api = Api()
    app = create_app()
    app.app_context().push()
    from src.resources.User import NewUser
    api.add_resource(NewUser, "/api/v1/user/create", endpoint="create_new_user", methods=['POST'])
    api.init_app(app)
    return app


def test_post_new_user_valid():
    app = create_api()
    with app.test_client() as test_client:
        response = test_client.post('/api/v1/user/create', json={
            "first_name": "John",
            "last_name": "Smith",
            "email": "t37test.up207056@myport.ac.uk",
            "password": "password123*",
            "login_method": "email",
            "current_mpg": 24.1,
            "current_city": 2,
            "oauthid": None
        })
        assert response.status_code == 200
        assert response.json["error"] == False
        assert response.json["messages"] == ["Successfully added new user"]
        from src.models import db
        from src.models.tables import User
        user = db.session.query(User).filter(User.email == "t37test.up207056@myport.ac.uk").first()
        assert user.email == "t37test.up207056@myport.ac.uk"
        assert user.firstname == "John"
        assert user.lastname == "Smith"
        assert user.logintype == "email"
        assert bcrypt.checkpw("password123*".encode("utf-8"), user.passwordenc.encode("utf-8"))
        assert user.currentmpg == 24.1
        assert user.currentcityid == 2
        db.session.query(User).filter(User.userid == user.userid).delete()
        db.session.commit()
