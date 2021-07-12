from flask import jsonify

from app.models.categories_model import CategoriesModel


def return_data() -> dict:

    data_category: list[CategoriesModel] = CategoriesModel.query.all()

    category_list = []
    for category in data_category:
        cat = {
           "category": {
               "name": category.name,
               "description": category.description,
               "task": [
                   {
                       "name": task.name,
                       "description": task.description,
                       "priority": task.eisenhower.type
                   }
                   for task in category.task_list

               ]
           } 
        }
        category_list.append(cat)
    
    return jsonify(category_list)