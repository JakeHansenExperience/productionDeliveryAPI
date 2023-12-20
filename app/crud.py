from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas

def get_deliveries(db: Session ):
    return db.query(models.Delivery).all()

def create_delivery(db: Session, delivery: schemas.DeliveryCreate):
    db_delivery = models.Delivery(address=delivery.address,time=delivery.time,driver=delivery.driver,lat=delivery.lat,long=delivery.long)
    db.add(db_delivery)
    db.commit()
    db.refresh(db_delivery)
    return db_delivery

def delete_delivery(db: Session, idd: schemas.DeleteDriver):
    try:
        deleteDelivery = db.query(models.Delivery).filter(models.Delivery.id == idd.id).first()
        db.delete(deleteDelivery)
        db.commit()
    except:
        raise HTTPException(status_code=404, detail="no such delivery")
    
def update_driver(db: Session, update: schemas.UpdateDriver):
    delivery = db.query(models.Delivery).filter(models.Delivery.id == update.id).first()
    delivery.driver = update.name
    db.commit()
    db.refresh(delivery)
    return delivery
