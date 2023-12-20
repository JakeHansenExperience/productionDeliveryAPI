from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/delivery", response_model=schemas.Delivery)
def create_delivery(delivery: schemas.DeliveryCreate, db: Session = Depends(get_db)):
    return crud.create_delivery(db=db, delivery=delivery)

@app.get("/deliveries", response_model=List[schemas.Delivery])
def get_deliveries(db: Session = Depends(get_db)):
    deliveries = crud.get_deliveries(db)
    return deliveries

@app.put("/deleteDelivery")
def delete_delivery(id: schemas.DeleteDriver, db: Session = Depends(get_db)):
   print(id)
   return crud.delete_delivery(db=db, idd=id)

@app.put("/updateDriver")
def updateDriver(update: schemas.UpdateDriver, db: Session = Depends(get_db)):
    return crud.update_driver(db=db, update=update)