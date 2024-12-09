import streamlit as st
from backend import (
    get_flavors, add_or_update_ingredient, add_allergen, add_customer_suggestion,
    add_to_cart, view_cart, remove_from_cart
)

# Application Title
st.set_page_config(page_title="Ice Cream Parlor", layout="wide")
st.title("🍨 Ice Cream Parlor Management System")

# Sidebar Menu
st.sidebar.header("Navigation")
menu = st.sidebar.radio(
    "Select a section:",
    ["View Flavors", "Manage Ingredients", "Add Allergens", "Customer Suggestions", "Cart Management"]
)

# 1. View Flavors Section
if menu == "View Flavors":
    st.header("🍦 Seasonal and Regular Flavors")
    
    # Filter Options
    filter_option = st.radio("Filter by:", ["All Flavors", "Seasonal Flavors"], horizontal=True)
    seasonal_only = filter_option == "Seasonal Flavors"
    search_keyword = st.text_input("Search flavors by name:")
    
    # Fetch and Display Flavors
    flavors = get_flavors(seasonal_only=seasonal_only)
    if search_keyword:
        flavors = [flavor for flavor in flavors if search_keyword.lower() in flavor[1].lower()]

    if flavors:
        for flavor in flavors:
            st.write(f"🍦 **{flavor[1]}** {'(Seasonal)' if flavor[2] else ''}")
    else:
        st.warning("No matching flavors found.")

# 2. Manage Ingredients Section
elif menu == "Manage Ingredients":
    st.header("🛠️ Manage Ingredients")
    
    # Input Fields for Ingredient Management
    ingredient_name = st.text_input("Ingredient Name")
    quantity = st.number_input("Quantity (in stock)", min_value=1, step=1)
    
    if st.button("Add or Update Ingredient"):
        if ingredient_name:
            message = add_or_update_ingredient(ingredient_name, quantity)
            st.success(message)
        else:
            st.error("Please enter a valid ingredient name.")

# 3. Add Allergens Section
elif menu == "Add Allergens":
    st.header("⚠️ Add New Allergens")
    
    # Input for Allergen
    allergen_name = st.text_input("Allergen Name")
    
    if st.button("Add Allergen"):
        if allergen_name:
            message = add_allergen(allergen_name)
            st.success(message)
        else:
            st.error("Please enter a valid allergen name.")

# 4. Customer Suggestions Section
elif menu == "Customer Suggestions":
    st.header("💬 Submit Customer Suggestions")
    
    # Inputs for Suggestion
    customer_name = st.text_input("Customer Name")
    suggestion = st.text_area("Flavor Suggestion")
    allergy_concern = st.text_input("Allergy Concern (Optional)")
    
    if st.button("Submit Suggestion"):
        if customer_name and suggestion:
            message = add_customer_suggestion(customer_name, suggestion, allergy_concern)
            st.success(message)
        else:
            st.error("Please provide both a name and a suggestion.")

# 5. Cart Management Section
elif menu == "Cart Management":
    st.header("🛒 Cart Management")
    
    cart_action = st.radio("Choose an action:", ["View Cart", "Add to Cart", "Remove from Cart"], horizontal=True)
    
    if cart_action == "View Cart":
        cart_items = view_cart()
        if cart_items:
            for item in cart_items:
                st.write(f"- **{item[1]}**: {item[2]} units")
        else:
            st.info("Your cart is empty.")
    
    elif cart_action == "Add to Cart":
        flavor_id = st.number_input("Flavor ID", min_value=1, step=1)
        quantity = st.number_input("Quantity", min_value=1, step=1)
        if st.button("Add to Cart"):
            message = add_to_cart(flavor_id, quantity)
            st.success(message)
    
    elif cart_action == "Remove from Cart":
        flavor_id = st.number_input("Flavor ID to Remove", min_value=1, step=1)
        if st.button("Remove from Cart"):
            message = remove_from_cart(flavor_id)
            st.success(message)
