from flask import request, current_app, jsonify

from app.services.helper_service import verify_required_key, verify_missing_key, verify_value_option

from app.services.eisenhower_service import verify_eisenhower

from app.models.tasks_model import TasksModel
from app.exc.missing_key import MissingKeyError
from app.exc.required_key import RequiredKeyError
from app.exc.different_value import InvalidOptionError

from app.models.eisenhowers_model import EisenhowerModel


def verify_values():
    
    required_keys = ["name", "description", "duration", "importance", "urgency"]

    value_options = [1, 2]

    session = current_app.db.session

    data = request.get_json()

    importance = data["importance"]
    urgency = data["urgency"]


    if verify_missing_key(data, required_keys):
        raise MissingKeyError(data, required_keys)

    if verify_required_key(data, required_keys):
        raise RequiredKeyError(data, required_keys)

    if not verify_value_option(data, value_options):
        raise InvalidOptionError(importance, urgency, value_options)


    verify_eisenhower()


    if importance == 1 and urgency == 1:
        
        eisenhower = EisenhowerModel.query.filter_by(type="Do It First").first()
    
    elif importance == 1 and urgency == 2:

        eisenhower = EisenhowerModel.query.filter_by(type="Delegate It").first()

    elif importance == 2 and urgency == 1:

        eisenhower = EisenhowerModel.query.filter_by(type="Schedule It").first()

    elif importance == 2 and urgency == 2:

        eisenhower = EisenhowerModel.query.filter_by(type="Delete It").first()

    
    tasks = TasksModel(eisenhower_id=eisenhower.id, **data)

    session.add(tasks)
    session.commit()

    return {
        "name": tasks.name,
        "description": tasks.description,
        "duration": tasks.duration,
        "eisenhower_classification": eisenhower.type
    }
