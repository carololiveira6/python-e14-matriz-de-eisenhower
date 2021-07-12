from flask import Blueprint, request

from app.exc import RequiredKeyError, MissingKeyError
from http import HTTPStatus

from app.services.tasks_categories_service import join_values

bp = Blueprint("tasks_categories", __name__)

@bp.route("/task_category", methods=["POST"])
def pivot_table():
    
    data = request.get_json()

    try:
        return join_values(data), HTTPStatus.CREATED
    
    except RequiredKeyError as e:
        return e.message

    except MissingKeyError as e:
        return e.message
