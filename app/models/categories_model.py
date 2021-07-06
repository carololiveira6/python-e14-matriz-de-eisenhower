from sqlalchemy import Column, Integer, String, Text

from dataclasses import dataclass
from sqlalchemy.orm import relationship

from app.configs.database import db


@dataclass
class CategoriesModel(db.Model):
    name: str
    description: str

    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)

    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    
    task_list = relationship(
        "TasksModel", backref="category_list", secondary="tasks_categories")