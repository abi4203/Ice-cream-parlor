import sqlite3

# Connect to the database
DB_FILE = 'icecream.db'

def connect_db():
    return sqlite3.connect(DB_FILE)

# Fetch all flavors
def get_flavors(seasonal_only=False):
    conn = connect_db()
    c = conn.cursor()
    if seasonal_only:
        c.execute("SELECT * FROM flavors WHERE is_seasonal = 1")
    else:
        c.execute("SELECT * FROM flavors")
    flavors = c.fetchall()
    conn.close()
    return flavors

# Add or update ingredient inventory
def add_or_update_ingredient(name, quantity):
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM ingredients WHERE name = ?", (name,))
    result = c.fetchone()
    if result:
        c.execute("UPDATE ingredients SET quantity = quantity + ? WHERE name = ?", (quantity, name))
    else:
        c.execute("INSERT INTO ingredients (name, quantity) VALUES (?, ?)", (name, quantity))
    conn.commit()
    conn.close()
    return f"Ingredient '{name}' updated successfully."

# Add a new allergen
def add_allergen(name):
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM allergens WHERE name = ?", (name,))
    if c.fetchone():
        conn.close()
        return f"Allergen '{name}' already exists."
    c.execute("INSERT INTO allergens (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
    return f"Allergen '{name}' added successfully."

# Add a customer suggestion
def add_customer_suggestion(customer_name, suggestion, allergy_concern=None):
    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO customer_suggestions (customer_name, suggestion, allergy_concern) VALUES (?, ?, ?)",
              (customer_name, suggestion, allergy_concern))
    conn.commit()
    conn.close()
    return "Suggestion added successfully."

# Add a flavor to the cart or updates the quantity.
def add_to_cart(flavor_id, quantity):
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM cart WHERE flavor_id = ?", (flavor_id,))
    result = c.fetchone()
    if result:
        c.execute("UPDATE cart SET quantity = quantity + ? WHERE flavor_id = ?", (quantity, flavor_id))
    else:
        c.execute("INSERT INTO cart (flavor_id, quantity) VALUES (?, ?)", (flavor_id, quantity))
    conn.commit()
    conn.close()
    return "Item added to cart."

# Remove an item from the cart.
def remove_from_cart(flavor_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute("DELETE FROM cart WHERE flavor_id = ?", (flavor_id,))
    conn.commit()
    conn.close()
    return "Item removed from cart."

# Displays all items in the cart along with flavor names and quantities.
def view_cart():
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT cart.id, flavors.name, cart.quantity FROM cart JOIN flavors ON cart.flavor_id = flavors.id")
    cart_items = c.fetchall()
    conn.close()
    return cart_items
