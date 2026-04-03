from sqlalchemy import Column, Integer, String, Date
from .database import Base
import datetime

class PantryItem(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)      # e.g., "Eggs"
    quantity = Column(String)             # e.g., "1 dozen" or "300ml"
    expiry_date = Column(Date)            # When does it go bad?
    
    # Simple logic: Is it expired?
    @property
    def is_expired(self):
        return self.expiry_date < datetime.date.today()