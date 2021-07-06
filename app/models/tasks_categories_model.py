from sqlalchemy import Column, Integer
from sqlalchemy.sql.schema import ForeignKey

from app.configs.database import db


class TasksCategories(db.Model):
    __tablename__ = "tasks_categories"

    id = Column(Integer, primary_key=True)
    
    task_id = Column(Integer, ForeignKey("tasks.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    