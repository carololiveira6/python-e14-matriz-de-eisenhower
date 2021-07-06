from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()


def init_app(app: Flask):

    db.init_app(app)
    app.db = db
    

    from app.models.eisenhowers_model import EisenhowerModel
    from app.models.categories_model import CategoriesModel
    from app.models.tasks_model import TasksModel
    from app.models.tasks_categories_model import TasksCategories