import pytest
from app import Database, Flavor  

@pytest.fixture
def setup_db():
    """Fixture to setup a new database connection"""
    db = Database("test.db")  
    yield db
    db.close()

def test_add_flavor_to_db(setup_db):
    """Test adding a flavor to the database"""
    flavor = Flavor(name="Mint", price=3)
    setup_db.add_flavor(flavor)
    
    # Fetch the flavor from DB to verify it was added
    db_flavor = setup_db.get_flavor_by_name("Mint")
    assert db_flavor is not None
    assert db_flavor.name == "Mint"

def test_retrieve_all_flavors(setup_db):
    """Test retrieving all flavors from the database"""
    setup_db.add_flavor(Flavor(name="Chocolate", price=5))
    setup_db.add_flavor(Flavor(name="Vanilla", price=4))
    
    flavors = setup_db.get_all_flavors()
    assert len(flavors) == 2
    assert "Chocolate" in [flavor.name for flavor in flavors]
    assert "Vanilla" in [flavor.name for flavor in flavors]
