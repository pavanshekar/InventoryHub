# InventoryHub

InventoryHub is a Django-based backend application for managing inventory items. It provides RESTful APIs for CRUD operations on items, categories, and tags.

## Features

- Create, read, update, and delete inventory items
- Manage categories and tags associated with items
- Authentication and authorization using token-based authentication
- Filtering and searching items based on various parameters

## Technologies Used

- Django: Backend framework for building web applications in Python
- Django REST Framework (DRF): Toolkit for building RESTful APIs in Django
- PostgreSQL: Relational database management system
- Heroku: Cloud platform for deploying, managing, and scaling web applications
- Swagger: Interactive API documentation tool for REST APIs

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/pavanshekar/InventoryHub.git
    cd InventoryHub
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

## API Documentation

The API documentation is available through Swagger at [Swagger UI](https://app.swaggerhub.com/apis/PAVANSOMASHEKAR97/inventory-hub_api/v1).

## Deployment

This application is deployed on Heroku. You can access the live version at [InventoryHub Heroku](https://inventory-hub-ec1eadc4cca1.herokuapp.com/).
