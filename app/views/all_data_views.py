from flask import Blueprint
from http import HTTPStatus

from app.services.all_data_service import return_data


bp = Blueprint("get_data", __name__)

@bp.route("/", methods=["GET"])
def return_all():
    
    return return_data(), HTTPStatus.OK
    