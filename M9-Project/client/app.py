import streamlit as st
import api_client
import datetime

# Page configuration
st.set_page_config(page_title="Smart Pantry", page_icon="🍳", layout="centered")

st.title("🍳 Smart Pantry & Recipe Finder")
st.write("Track your food, reduce waste, and find delicious recipes!")

# Create two tabs for a clean UI
tab1, tab2 = st.tabs(["🛒 My Pantry", "👨‍🍳 Find Recipes"])

# --- TAB 1: INVENTORY MANAGEMENT ---
with tab1:
    st.header("Add a New Item")
    
    # A form to input new food
    with st.form("add_item_form", clear_on_submit=True):
        name = st.text_input("Item Name (e.g., Chicken, Milk, Rice)")
        quantity = st.text_input("Quantity (e.g., 500g, 1 kg, 1 liter)")
        expiry = st.date_input("Expiration Date", min_value=datetime.date.today())
        
        submit = st.form_submit_button("Add to Pantry")
        
        if submit and name and quantity:
            api_client.add_item(name, quantity, expiry)
            st.success(f"Successfully added {name} to your pantry!")

    st.divider()
    
    st.header("What's in the fridge?")
    inventory = api_client.get_inventory()
    
    if inventory:
        today = datetime.date.today()
        fresh_items = []
        expired_items = []
        
        # 1. Sort the items into the two lists
        for item in inventory:
            exp_date = datetime.datetime.strptime(item['expiry_date'], "%Y-%m-%d").date()
            if exp_date < today:
                expired_items.append(item)
            else:
                fresh_items.append(item)
                
        # 2. Display all the FRESH food at the top
        for item in fresh_items:
            st.write(f"🏷️ **{item['name']}** — {item['quantity']} (Expires: {item['expiry_date']})")
            
        # 3. Display all the EXPIRED food at the bottom
        for item in expired_items:
            st.markdown(f"🚨 :red[**{item['name']}** — {item['quantity']} (EXPIRED: {item['expiry_date']})]")
            
    else:
        # This lines up perfectly with 'if inventory:' so it only shows if the database is actually empty
        st.info("Your pantry is empty. Add some items above!")

# --- TAB 2: RECIPE SUGGESTIONS ---
with tab2:
    st.header("What can I cook today?")
    st.write("Click the button below to search Spoonacular based on your fresh ingredients.")
    
    if st.button("🔍 Find Recipes", type="primary"):
        with st.spinner("Asking the chef..."):
            data = api_client.get_recipes()
            
            if "message" in data:
                st.warning(data["message"]) # e.g., "No fresh ingredients!"
                
            elif "suggested_recipes" in data:
                recipes_data = data["suggested_recipes"]
                
                # Check if Spoonacular sent back an error instead of a list
                if isinstance(recipes_data, dict) and "error" in recipes_data:
                    st.error("Spoonacular API Error: Check your API key in the .env file!")
                else:
                    ingredients_used = data.get("ingredients_used", [])
                    st.success(f"Found recipes using: {', '.join(ingredients_used)}")
                    
                    # Loop through the recipes and display them
                    for recipe in recipes_data:
                        st.subheader(recipe["title"])
                        st.image(recipe["image"], width=400)
                        
                        # Spoonacular tells us what we are missing
                        missed = [i["name"] for i in recipe.get("missedIngredients", [])]
                        if missed:
                            st.warning(f"🛒 **You still need to buy:** {', '.join(missed)}")
                        else:
                            st.success("✅ You have all the ingredients for this!")
                        st.divider()