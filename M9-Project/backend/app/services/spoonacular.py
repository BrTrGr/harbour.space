import os
import requests
from dotenv import load_dotenv

# Load the secret key from the .env file
load_dotenv()
API_KEY = "863d8d840ae34e14b847021c3c76d1fe"
BASE_URL = "https://api.spoonacular.com/recipes/findByIngredients"

def get_recipes_by_ingredients(ingredients: list[str]):
    # Join the list of ingredients into a comma-separated string (e.g., "eggs,milk,flour")
    ingredients_string = ",".join(ingredients)
    
    # Set up the parameters for the Spoonacular API
    params = {
        "apiKey": API_KEY,
        "ingredients": ingredients_string,
        "number": 3,  # Let's just ask for 3 recipes so it's not overwhelming
        "ranking": 1  # Maximize used ingredients
    }
    
    # Make the request to Spoonacular
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not fetch recipes from Spoonacular."}