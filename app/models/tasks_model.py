from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.sql.schema import ForeignKey

from dataclasses import dataclass

from app.configs.database import db


@dataclass
class TasksModel(db.Model):
    name: str
    description: str
    duration: int
 
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)

    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    duration = Column(Integer)
    importance = Column(Integer)
    urgency = Column(Integer)
    
    eisenhower_id = Column(Integer, ForeignKey("eisenhowers.id"))
