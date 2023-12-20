from typing import List, Union, Optional

from pydantic import BaseModel

class Delivery(BaseModel):
    id: int
    address: str
    time: str
    driver: str
    lat: str
    long: str

    class Config:
        orm_mode = True

class DeliveryCreate(BaseModel):
    address: str
    time: str
    driver: str
    lat: str
    long: str

class UpdateDriver(BaseModel):
    id: int
    name: str

class DeleteDriver(BaseModel):
    id: int