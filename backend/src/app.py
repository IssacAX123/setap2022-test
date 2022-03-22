import os

from flask import Flask, render_template
from flask_restful import Api
from endpoints.task import Task
import logging

app = Flask(__name__)
api = Api(app)

if not app.debug:
    logging.basicConfig(filename='logs/logs.log', level=logging.WARNING,
                        format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
    logging.info('\n')

api.add_resource(Task, "/api/v1/task/<string:user_id>/<string:task_id>", endpoint="get-task",
                 methods=["GET", "DELETE"],
                 resource_class_kwargs={"mysql": "mysql", "api": api})
api.add_resource(Task, "/api/v1/task/create", endpoint="create_task", methods=["POST"],
                 resource_class_kwargs={"mysql": "mysql", "api": api})

api.add_resource(Task, "/api/v1/task/<string:user_id>/<string:task_id>", endpoint="update-task", methods=["PATCH"],
                 resource_class_kwargs={"mysql": "mysql", "api": api})

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
