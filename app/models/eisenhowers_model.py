from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

from app.configs.database import db


class EisenhowerModel(db.Model):
    __tablename__ = "eisenhowers"

    id = Column(Integer, primary_key=True)

    type = Column(String(100))

    task_list = relationship(
        "TasksModel", backref=backref("eisenhower", uselist=False))
