from app.exc.missing_key import MissingKeyError
from app.exc.required_key import RequiredKeyError

from app.services.helper_service import verify_required_key, verify_missing_key

from flask import request, current_app, jsonify

from app.models.categories_model import CategoriesModel


def create_category():

    required_key = ["name", "description"]

    session = current_app.db.session

    data = request.get_json()

    if verify_missing_key(data, required_key):
        raise MissingKeyError(data, required_key)

    if verify_required_key(data, required_key):
        raise RequiredKeyError(data, required_key)

    category = CategoriesModel(**data)

    session.add(category)
    session.commit()

    return jsonify(category)