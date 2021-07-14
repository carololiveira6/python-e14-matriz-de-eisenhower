from flask import Blueprint

from app.exc import RequiredKeyError, MissingKeyError, InvalidOptionError
from http import HTTPStatus

from app.services.task_service import verify_values

bp = Blueprint("tasks", __name__)

@bp.route("/task", methods=["POST"])
def importance_or_urgency():
    
    try:
        return verify_values(), HTTPStatus.CREATED

    except RequiredKeyError as e:
        return e.message

    except MissingKeyError as e:
        return e.message
    
    except InvalidOptionError as e:
        return e.message