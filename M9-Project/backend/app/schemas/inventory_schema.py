from pydantic import BaseModel
from datetime import date
from typing import Optional

# This defines what data we need to CREATE an item
class ItemCreate(BaseModel):
    name: str
    quantity: str
    expiry_date: date

# This defines what an item looks like when we READ it (it includes an ID)
class ItemResponse(ItemCreate):
    id: int

    class Config:
        from_attributes = True