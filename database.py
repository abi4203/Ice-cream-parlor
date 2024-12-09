import sqlite3

# Connect to SQLite database (or create it if it doesn’t exist)
def create_database():
    conn = sqlite3.connect('icecream.db')
    c = conn.cursor()

    # Create Flavors table
    c.execute('''
        CREATE TABLE IF NOT EXISTS flavors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            is_seasonal INTEGER NOT NULL
        )
    ''')

    # Create Ingredients table
    c.execute('''
        CREATE TABLE IF NOT EXISTS ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')

    # Create Allergens table
    c.execute('''
        CREATE TABLE IF NOT EXISTS allergens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    # Create Customer Suggestions table
    c.execute('''
        CREATE TABLE IF NOT EXISTS customer_suggestions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            suggestion TEXT NOT NULL,
            allergy_concern TEXT
        )
    ''')

    # Create Cart table
    c.execute('''
        CREATE TABLE IF NOT EXISTS cart (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flavor_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY (flavor_id) REFERENCES flavors (id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Database and tables created successfully.")

# Function to populate sample data for testing
def populate_sample_data():
    conn = sqlite3.connect('icecream.db')
    c = conn.cursor()

    # Insert sample flavors
    c.execute("INSERT INTO flavors (name, is_seasonal) VALUES ('Vanilla', 0)")
    c.execute("INSERT INTO flavors (name, is_seasonal) VALUES ('Mango', 1)")
    c.execute("INSERT INTO flavors (name, is_seasonal) VALUES ('Chocolate', 0)")

    # Insert sample ingredients
    c.execute("INSERT INTO ingredients (name, quantity) VALUES ('Milk', 50)")
    c.execute("INSERT INTO ingredients (name, quantity) VALUES ('Sugar', 30)")
    c.execute("INSERT INTO ingredients (name, quantity) VALUES ('Cocoa', 20)")

    # Insert sample allergens
    c.execute("INSERT INTO allergens (name) VALUES ('Nuts')")
    c.execute("INSERT INTO allergens (name) VALUES ('Gluten')")

    # Commit changes and close
    conn.commit()
    conn.close()
    print("Sample data added successfully.")

if __name__ == "__main__":
    create_database()   
    populate_sample_data()  
