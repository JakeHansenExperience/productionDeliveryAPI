from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Delivery(Base):
    __tablename__ = "deliveries"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String)
    time = Column(String)
    driver = Column(String)
    lat = Column(String)
    long = Column(String)