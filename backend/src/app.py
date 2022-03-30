import os
import logging
import sys
from decouple import config

from flask import Flask
from flask_restful import Api
try:
    from src.models import db
except:
    from models import db

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = config("DB_URI")
    db.init_app(app)
    if not app.debug:
        logging.basicConfig(filename='logs/logs.log', level=logging.WARNING,
                            format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
        logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
        logging.info('\n')
    return app


if __name__ == "__main__":
    api = Api()
    app = create_app()
    app.app_context().push()
    try:
        from src.resources.User import NewUser
    except:
        from resources.User import NewUser

    api.add_resource(NewUser, "/api/v1/user/create", endpoint="create_new_user", methods=['POST'])
    api.init_app(app)
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
