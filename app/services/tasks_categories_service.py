from flask import current_app, request

from app.services.helper_service import verify_required_key, verify_missing_key

from app.exc.missing_key import MissingKeyError
from app.exc.required_key import RequiredKeyError

from app.models.categories_model import CategoriesModel
from app.models.tasks_model import TasksModel
from app.models.tasks_categories_model import TasksCategories

def join_values(data: dict):

    required_keys = ["category_name", "task_name"]

    session = current_app.db.session

    data = request.get_json()

    if verify_missing_key(data, required_keys):
        raise MissingKeyError(data, required_keys)

    if verify_required_key(data, required_keys):
        raise RequiredKeyError(data, required_keys)

    
    task: TasksModel = TasksModel.query.filter_by(name=data["task_name"]).first()
    category: CategoriesModel = CategoriesModel.query.filter_by(name=data["category_name"]).first()

    task_category = TasksCategories(category_id=category.id, task_id=task.id)

    session.add(task_category)
    session.commit()


    return {
        "category_name": category.name,
        "task_name": task.name,
        "eisenhower_classification": task.eisenhower.type
    }