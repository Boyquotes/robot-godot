from models.base import Base
from sqlalchemy import Integer, Float, Column

class Position(Base):
    __tablename__ = "robot_positions"

    id = Column(Integer, primary_key=True)
    x = Column(Float)
    y = Column(Float)
    z = Column(Float)
    r = Column(Float)

    def pos_as_json(self):
        return {
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "z": self.z,
            "r": self.r
        }

    def __repr__(self) -> str:
        return f"id = {self.id}, x = {self.x}, y = {self.y}, z = {self.z}, rotation = {self.r}"