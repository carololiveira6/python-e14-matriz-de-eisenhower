from flask import Blueprint

# from app.exc import 
from http import HTTPStatus

# from app.services.task_service import

bp = Blueprint("categories", __name__)

@bp.route("/category", methods=["POST"])
def importance_or_urgency():
    ...