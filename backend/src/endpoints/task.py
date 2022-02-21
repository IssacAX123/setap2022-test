from flask_restful import Resource
from flask import jsonify, make_response, request

class Task(Resource):
    """Task Class representing all endpoints related to tasks

    Task class has the following methods:
    GET / .get() to get get task details
    POST / .post() to add a new task
    PATCH / .patch() to update an existing task
    DELETE / .delete() to delete a task

    Args:
        **kwargs: Arbitrary keyword arguments.

    Attributes:
        mysql (:obj:`flask_mysqldb.MySQL`): MySQL that was instantiated with app to get the cursor
        cursor (:obj:`flask_mysqldb.MySQL.connection.cursor`): this object allows to execute SQL commands

    """
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.mysql = "mysql"
        self.cursor = "cursor"
        Task.api = kwargs["api"]

    def get(self, user_id, task_id):
        """ endpoint = /api/v1/task/<string:user_id>/<string:task_id>

        Args:
            user_id (str): id that identifies the user
            task_id (str): id that identifies the task

        Returns:
            :obj:`flask.wrappers.Response`: a Response object containing success/error message and status code
        """
        return make_response(jsonify({"response": "success", "task": "details"}), 200)

    def post(self):
        """ endpoint = /api/v1/task/create

        Recieves form containing 'user_id, 'name', 'due_date' and then add a new Task to database

        Returns:
            :obj:`flask.wrappers.Response`: a Response object containing success/error message and status code
        """
        # user_id = request.json["user_id"]
        # name = request.json["name"]
        # due_date = request.json["due_date"]
        return make_response(jsonify({"response": "success"}), 200)

    def patch(self, user_id, task_id):
        for key in request.json:
            value = request.json[key]
        return make_response(jsonify({"response": "success"}), 200)

    def delete(self, user_id, task_id):
        return make_response(jsonify({"response": "success"}), 200)

