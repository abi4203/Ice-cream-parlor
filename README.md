# Ice Cream Parlor App

This is a simple Python application for managing an ice cream parlor cafe, using SQLite for managing seasonal flavor offerings, ingredient inventory, customer flavor suggestions, and allergy concerns.

## Features

- **Seasonal Flavor Offerings**: Manage seasonal ice cream flavors.
- **Ingredient Inventory**: Keep track of the ingredients available for each flavor.
- **Customer Suggestions**: Allow customers to suggest new flavors and provide feedback on existing ones.
- **Allergy Concerns**: Add and manage allergens for each flavor.
- **Shopping Cart**: Maintain a cart of your favorite products and quantities.
- **Search and Filter**: Search for flavors and filter based on preferences.
- **Add Allergens**: Add allergens that don't already exist in the database.

## Requirements

To run the application, you need Python 3.x and Docker installed on your machine.

### Dependencies

- Python 3.x
- Streamlit (for the UI)
- SQLite3 (for database management)
- pandas (for data handling)
- numpy (for numerical operations)
- pytest (for unit testing)

### Installation Steps

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/ice-cream-parlor.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ice-cream-parlor
    ```

3. Create and activate a Python virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use '.env\Scriptsctivate'
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the application:

    ```bash
    streamlit run app.py
    ```

   This will start the Streamlit application and open it in your default web browser.

### Database Setup

The application uses SQLite to store data. The database (`ice_cream_parlor.db`) will be created automatically when the application runs for the first time. You can inspect or manage the database by:

1. Using SQLite tools (e.g., DB Browser for SQLite) to open `ice_cream_parlor.db`.
2. Running queries through the SQLite command line interface.

### Running the Application with Docker

To run the application in a Docker container, follow these steps:

1. Build the Docker image:

    ```bash
    docker build -t ice-cream-parlor-app .
    ```

2. Run the Docker container:

    ```bash
    docker run -p 8501:8501 ice-cream-parlor-app
    ```

   This will start the application in a Docker container. Open your browser and visit `http://localhost:8501` to access the app.

## Testing

The application includes basic unit tests to verify the functionality of core features like adding items to the cart, removing items, and interacting with the database.

To run the tests, use the following command:

```bash
pip install pytest  # If pytest is not already installed
pytest
```

You can find the test files in the `tests/` folder. These tests cover core functionality such as:
- Adding items to the cart
- Removing items from the cart
- Interacting with the database (e.g., adding and retrieving flavors)

## Documentation of Code

The code is documented with comments to explain the purpose and logic behind the key functions. Each function and module has docstrings to enhance readability and maintainability.

## Docker Instructions

The project includes a `Dockerfile` to build a Docker container for the application. Follow the instructions above to build and run the application within Docker.

### Docker Build:

```bash
docker build -t ice-cream-parlor-app .
```

### Docker Run:

```bash
docker run -p 8501:8501 ice-cream-parlor-app
```

