# Maja's Merchandise Store

This is an e-commerce website built with Django, dedicated to selling merchandise for Maja the dog.

## Project Structure

The project is structured into four main apps:
- `home`: The main landing page.
- `store`: Handles the products, categories, and reviews.
- `accounts`: Manages user authentication (login, logout, signup).
- `cart`: Implements the shopping cart functionality.

## How to Run the Project

1.  **Navigate to the `maja` directory:**
    ```bash
    cd maja
    ```

2.  **Apply the database migrations:**
    ```bash
    python3 manage.py migrate
    ```

3.  **Start the development server:**
    ```bash
    python3 manage.py runserver
    ```

4.  **Open the website:**
    Open a web browser and go to `http://127.0.0.1:8000/`.

## What has been done

*   Created a new Django project named `maja`.
*   Created four apps: `store`, `cart`, `accounts`, and `home`.
*   Adapted the models from the `moviesstore` project to the new `maja` project.
*   Created views and templates for the `store`, `accounts`, and `home` apps.
*   Implemented a shopping cart using sessions.
*   Created a base template for a consistent look and feel.
*   Added static files for styling.
*   The logo image at `maja/maja/static/img/logo.png` is a placeholder. You should replace it with your own logo.
