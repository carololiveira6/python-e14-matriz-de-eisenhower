from flask import Blueprint

from app.exc import RequiredKeyError, MissingKeyError
from http import HTTPStatus

from app.services.categories_service import create_category

bp = Blueprint("categories", __name__)

@bp.route("/category", methods=["POST"])
def create_data():

    try:
        return create_category(), HTTPStatus.CREATED

    except RequiredKeyError as e:
        return e.message

    except MissingKeyError as e:
        return e.message
