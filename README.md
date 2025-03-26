# e_commerce_api
Django REST API for a comprehensive e-commerce platform. This API facilitates both buying and selling functionalities, enabling users to sell and buy products.

Introduction

O-Mache is a complete e-commerce platform built with Django REST Framework for the backend and Vite React for the frontend. It provides a robust backend API for user account management, product listing, shopping cart, orders, and payment processing. The platform supports JWT authentication, product categorization, stock management, and order tracking functionalities.

System Architecture

O-Mache is built using:

-   Backend: Django REST Framework
-   Authentication: JWT token authentication via dj-rest-auth
-   Database Models: Customized Django models with relationship-based connections

API Endpoints

Authentication Endpoints

-   `127.0.0.1:8000/registration/`: User registration endpoint
-   JWT token endpoints from dj-rest-auth to verify and refresh the token

User Profile Endpoints

-   `127.0.0.1:8000/account/`: GET and UPDATE user profile
    -   Returns/accepts: `{first_name:"", last_name "", avatar "", gender ""}`

Product Listing Endpoints

-   `127.0.0.1:8000/`: Default endpoint returning products based on categories
    -   Returns: `{electronics:[], fashions:[], kitchen:[], computing:[], gaming:[], phonestablet:[]}`
-   `127.0.0.1:8000/product/search/?search=searchobject`: Search products endpoint
    -   Returns: List of products that match search query
-   `127.0.0.1:8000/product/{category}/`: Get products by category
    -   Categories: electronics, furniture, fashions, computing, gaming, kitchen, phones, sports
    -   Returns: List of products in specified category

 Product Management Endpoints

-   `127.0.0.1:8000/create/`: POST URL to create new product listings
    -   Accepts: `{name:"", image="", description="", category="", item_number="", price="", payment_mpesa_number=""}`

 Shopping and Order Endpoints

-   `127.0.0.1:8000/cart/`: POST URL for handling cart
    -   Accepts: List of product IDs
    -   Returns: Product details list of products in cart
-   `127.0.0.1:8000/cashout/`: POST endpoint to place orders
    -   Accepts: `{order:[{product:"", number:""}], mpesa_number:""}`
    -   Where `product` is the product's ID and `number` is the number
-   `127.0.0.1:8000/track/order/`: GET endpoint to track orders
    -   Returns: List of order tracking details

 Payment Integration

-   `127.0.0.1:8000/safwebhook/`: Webhook for payment processing integration
    -   Facilitates integration with payment gateways like M-Pesa and bank APIs

 Authentication

O-Mache uses JWT (JSON Web Token) authentication from dj-rest-auth:

1.  User registration through `/registration/` endpoint.
2.  Login to get JWT token.
3.  Include token in Authorization header of authenticated requests.
4.  Refresh and validate token handled by dj-rest-auth endpoints.

 Order Processing Flow

1.  Cart Creation:User adds products to cart.
2.  Checkout: User orders via `/cashout/` with product IDs, amount, and payment number.
3.  Order Creation: System generates `Order_Payment` and `Order_Track` records.
4.  Payment Processing: User pays via M-Pesa.
5.  Payment Verification:Payment confirmation via webhook.
6.  Order Status Updates: System updates order status via signals.
7.  Inventory Management:Stock levels updated upon successful purchase.

Signals and Hooks

O-Mache makes use of Django signals to provide automated processes:

1.  Order Creation Signal: Triggered when a new order is created.
    -   Extendable with additional business logic.
2.  Order Tracking Signal: Triggered when order status is changed.
    -   Updates `track_status` field in `Order_Track` model.
3.  Inventory Management Signal: Triggered after successful purchase.
    -   Automatically reduces product stock (`item_number`).

 Installation and Setup

Before proceeding, ensure you have Python and pip installed.

1.  Install Required Packages: Navigate to the `e_commerce_api/omachemainproj` directory and install the required packages from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

2.  Run Migrations and Create Superuser:After cloning the repository from GitHub, follow these steps to set up the project:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    ```

3.  Start the Development Server:

    ```bash
    python manage.py runserver
    ```

This will start the Django development server, and you can access the API endpoints at `http://127.0.0.1:8000/`.
