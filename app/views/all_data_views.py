from flask import Blueprint
from http import HTTPStatus


bp = Blueprint("tasks", __name__)

@bp.route("/", methods=["GET"])
def return_data():
    ...