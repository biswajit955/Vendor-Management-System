# Vendor Management System

This is a Vendor Management System developed using Django and Django REST Framework.

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/biswajit955/Vendor-Management-System.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the development server:

    ```bash
    python manage.py runserver
    ```

The API will be accessible at `http://127.0.0.1:8000/`. You can explore the API using tools like `curl`, `httpie`, or Postman.

If You Needed Django Admin `http://127.0.0.1:8000/admin/`.

    - **username:** admin
    - **Password:** 1

## API Endpoints

## Authentication Endpoints

### Obtain Token

- **Endpoint:** `/api/token/`
- **Method:** `POST`
- **Payload:**
    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```
- **Response:**
    ```json
    {
        "token": "your_access_token",
        "user_id": "your_user_id",
        "username": "your_username"
    }
    ```

### Logout

- **Endpoint:** `/api/logout/`
- **Method:** `POST`
- **Headers:**
    ```
    Authorization: Token your_access_token
    ```
- **Response:**
    ```json
    {
        "detail": "Successfully logged out."
    }
    ```

### Signup

- **Endpoint:** `/api/signup/`
- **Method:** `POST`
- **Payload:**
    ```json
    {
        "username": "new_username",
        "password": "new_password"
    }
    ```
- **Response:**
    ```json
    {
        "token": "new_access_token",
        "user_id": "new_user_id",
        "username": "new_username"
    }
    ```


### Vendor Endpoints

- **List all vendors:**

    - **Endpoint:** `/api/vendors/`
    - **Method:** `GET`
    - **Headers:**
    ```
    Authorization: Token "your_access_token"
    ```


- **Create a new vendor:**

    - **Endpoint:** `/api/vendors/`
    - **Method:** `POST`
    - **Headers:**
    ```
    Authorization: Token "your_access_token"
    ```


- **Retrieve a specific vendor's details:**

    - **Endpoint:** `/api/vendors/{vendor_id}/`
    - **Method:** `GET`
    - **Headers:**
    ```
    Authorization: Token "your_access_token"
    ```


- **Update a vendor's details:**

    - **Endpoint:** `/api/vendors/{vendor_id}/`
    - **Method:** `PUT`
    - **Headers:**
    ```
    Authorization: Token "your_access_token"
    ```

- **Delete a vendor:**

    - **Endpoint:** `/api/vendors/{vendor_id}/`
    - **Method:** `DELETE`
    - **Headers:**
    ```
    Authorization: Token "your_access_token"
    ```

- **Retrieve calculated performance metrics for a specific vendor:**

    - **Endpoint:** `/api/vendors/{vendor_id}/performance/`
    - **Method:** `GET`
    - **Headers:**
    ```
    Authorization: Token "your_access_token"
    ```

### Purchase Order Endpoints

- **List all purchase orders:**

    - **Endpoint:** `/api/purchase_orders/`
    - **Method:** `GET`
    - **Headers:**
    ```
    Authorization: Token "your_access_token"
    ```

- **Create a new purchase order:**

    - **Endpoint:** `/api/purchase_orders/`
    - **Method:** `POST`
    - **Headers:**
    ```
    Authorization: Token "your_access_token"
    ```

- **Retrieve details of a specific purchase order:**

    - **Endpoint:** `/api/purchase_orders/{po_id}/`
    - **Method:** `GET`
    - **Headers:**
    ```
    Authorization: Token "your_access_token"
    ```

- **Update a purchase order:**

    - **Endpoint:** `/api/purchase_orders/{po_id}/`
    - **Method:** `PUT`
    - **Headers:**
    ```
    Authorization: Token "your_access_token"
    ```

- **Delete a purchase order:**

    - **Endpoint:** `/api/purchase_orders/{po_id}/`
    - **Method:** `DELETE`
    - **Headers:**
    ```
    Authorization: Token "your_access_token"
    ```

- **Acknowledge a purchase order (update acknowledgment_date):**

    - **Endpoint:** `/api/purchase_orders/{po_id}/acknowledge/`
    - **Method:** `POST`
    - **Headers:**
    ```
    Authorization: Token "your_access_token"
    ```


## Additional Notes

- **Initial Database State:**
    - In the `Vendor` model, IDs 2-4 exist.
    - In the `PurchaseOrder` model, data with IDs 1-8 is available.
    - When you are working with URLs like `/api/purchase_orders/{po_id}/` or `/api/vendors/{vendor_id}/`, you may need these IDs.
    - If you have any doubts about the database, you can check the Django admin interface at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).
      - **Username:** admin
      - **Password:** 1

- Make sure to handle authentication and authorization according to your requirements.
- Update the models, views, and serializers as per your specific business logic.

Feel free to reach out if you have any questions or issues!
