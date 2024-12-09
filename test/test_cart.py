import pytest
from app import Cart, Flavor  # Adjust imports based on your application structure

@pytest.fixture
def setup_cart():
    """Fixture to setup a new cart for each test"""
    cart = Cart()
    return cart

def test_add_item_to_cart(setup_cart):
    """Test adding an item to the cart"""
    flavor = Flavor(name="Chocolate", price=5)
    setup_cart.add_item(flavor)
    
    assert len(setup_cart.items) == 1
    assert setup_cart.items[0] == flavor

def test_remove_item_from_cart(setup_cart):
    """Test removing an item from the cart"""
    flavor = Flavor(name="Vanilla", price=4)
    setup_cart.add_item(flavor)
    setup_cart.remove_item(flavor)
    
    assert len(setup_cart.items) == 0

def test_cart_total(setup_cart):
    """Test cart total calculation"""
    flavor1 = Flavor(name="Chocolate", price=5)
    flavor2 = Flavor(name="Vanilla", price=4)
    setup_cart.add_item(flavor1)
    setup_cart.add_item(flavor2)
    
    total = setup_cart.get_total()
    assert total == 9  # 5 + 4

def test_flavor_exists_in_database(setup_cart):
    """Test interacting with the database to check if flavor exists"""
    flavor = Flavor(name="Strawberry", price=6)
    # Assuming you have a method to add to DB and a method to check if it exists
    setup_cart.db.add_flavor(flavor)
    assert setup_cart.db.flavor_exists(flavor) is True
