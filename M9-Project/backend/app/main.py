from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date
from .services import spoonacular

# Import our other files
from .db import database, models
from .schemas import inventory_schema

# Create the database tables automatically
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Smart Pantry API")

# --- API LAYER: ENDPOINTS ---

@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Pantry API!"}

# Endpoint to see everything in the pantry
@app.get("/inventory/", response_model=list[inventory_schema.ItemResponse])
def get_inventory(db: Session = Depends(database.get_db)):
    return db.query(models.PantryItem).all()

# Endpoint to add a new item
@app.post("/inventory/", response_model=inventory_schema.ItemResponse)
def add_item(item: inventory_schema.ItemCreate, db: Session = Depends(database.get_db)):
    new_item = models.PantryItem(
        name=item.name, 
        quantity=item.quantity, 
        expiry_date=item.expiry_date
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

# --- APPLICATION LOGIC: EXPIRY CHECKER ---

@app.get("/inventory/status")
def check_pantry_status(db: Session = Depends(database.get_db)):
    items = db.query(models.PantryItem).all()
    today = date.today()
    
    expired_items = [i.name for i in items if i.expiry_date < today]
    fresh_items = [i.name for i in items if i.expiry_date >= today]
    
    return {
        "summary": f"You have {len(expired_items)} expired items.",
        "expired": expired_items,
        "fresh": fresh_items
    }
    


@app.get("/recipes/suggest")
def suggest_recipes(db: Session = Depends(database.get_db)):
    # 1. Get all items from the database
    items = db.query(models.PantryItem).all()
    today = date.today()
    
    # 2. Filter out the expired ones (we only want to cook with fresh food!)
    fresh_ingredients = [item.name for item in items if item.expiry_date >= today]
    
    if not fresh_ingredients:
        return {"message": "You have no fresh ingredients to cook with!"}
    
    # 3. Send the fresh ingredients to Spoonacular
    recipes = spoonacular.get_recipes_by_ingredients(fresh_ingredients)
    
    # 4. Return the recipes to the user!
    return {
        "ingredients_used": fresh_ingredients,
        "suggested_recipes": recipes
    }