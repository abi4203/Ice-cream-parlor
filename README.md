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

### Installation Steps

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/ice-cream-parlor-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ice-cream-parlor-app
    ```

3. Create and activate a Python virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use 'env\\Scripts\\activate'
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

The application uses SQLite to store data. The database will be created automatically when the application runs for the first time. However, you can manage and query the database using SQLite tools or command-line interface.

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

The application includes basic unit tests to verify the functionality of core features like adding items to the cart and filtering flavors. To run the tests, use the following command:

```bash
pytest
