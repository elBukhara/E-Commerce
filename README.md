# E-Commerce Backend

This is a backend service for an E-Commerce platform, built using FastAPI and SQLAlchemy. It includes functionalities like user management, item listing, categories, shopping cart management, and authentication/authorization systems. The project is still under development.

## Features

- FastAPI: A high-performance framework for building APIs with Python 3.7+.
- SQLAlchemy: ORM for database management.
- Authorization/Authentication (by [FastAPI-Users](https://github.com/fastapi-users/fastapi-users)):
    - BearerTransport for token-based authentication.
    - DatabaseStrategy for storing and verifying credentials.
- Users, Items, Categories, and Cart Models: Core models for the e-commerce functionality.
- Project structure is inspired by Django’s modular approach, making it easy to navigate and maintain.

## Project Structure

    .
    └── E-Commerce/
        ├── .venv                 # Virtual environment (local)
        ├── app/                  # Main application directory
        │   ├── __init__.py
        │   ├── auth              # Authentication system
        │   ├── cart              # Cart management module
        │   ├── category          # Item category module
        │   ├── items             # Item management module
        │   ├── users             # User-related module   
        │   ├── database.py       # Database connection setup
        │   └── main.py           # Entry point of the application
        ├── .gitignore            # Git ignore file
        └── requirements.txt      # Python dependencies

Each module has the following files (e.g. module `cart`):

    .
    └── cart/
        ├── __init__.py     
        ├── models.py           # Database models for carts
        ├── repository.py       # Data access layer for carts
        ├── routers.py          # API routes for cart operations
        └── schemas.py          # Pydantic schemas for cart data validation

## Installation

To set up this project on your local machine, follow the instructions below:

### Prerequisites

- Python 3.8 or higher
- `Poetry` or `pip` for dependency management

### Setup

    git clone https://github.com/elBukhara/E-Commerce
    cd E-Commerce
    python -m venv .venv
    .venv/Source/activate
    pip install -r requirements.txt

    cd app
    uvicorn main:app --reload

### Documentation

FastAPI provides interactive documentation, available at:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Authentication

This project uses a Bearer token strategy for authentication. Users need to authenticate using the API and will receive a token for subsequent requests.

- **BearerTransport**: Manages token transport.
- **DatabaseStrategy**: Handles storing user credentials and verifying login attempts.

## Models

- **User**: Manages user registration, login, and profile management.
- **Items**: Allows users to browse and manage items available for purchase.
- **Category**: Organizes items into different categories.
- **Cart**: Handles adding and removing items from the user's shopping cart.

## TODOs

- Integrate payment gateway.
- Implement advanced features like order tracking.
- Write unit tests.
- Improve database optimizations.

## Contributing

Feel free to open issues or submit pull requests. Contributions are welcome!