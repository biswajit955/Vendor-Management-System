# Vendor Management System

This is a Vendor Management System developed using Django and Django REST Framework.

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/biswajit955/Vendor-Management-System.git
    ```

2. Navigate to the project directory:

    ```bash
    cd vendor-management-system
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

The API will be accessible at `http://127.0.0.1:8000/`. You can explore the API using tools like `curl`, `httpie`, or Postman.

5. If You Needed Django Admin:

    ```bash
    python manage.py admin
    ```
    - **username:** admin
    - **Password:** 1

## API Endpoints

### Vendor Endpoints

- **List all vendors:**

    ```http
    GET /api/vendors/
    ```

- **Create a new vendor:**

    ```http
    POST /api/vendors/
    ```

- **Retrieve a specific vendor's details:**

    ```http
    GET /api/vendors/{vendor_id}/
    ```

- **Update a vendor's details:**

    ```http
    PUT /api/vendors/{vendor_id}/
    ```

- **Delete a vendor:**

    ```http
    DELETE /api/vendors/{vendor_id}/
    ```

- **Retrieve calculated performance metrics for a specific vendor:**

    ```http
    GET /api/vendors/{vendor_id}/performance/
    ```

### Purchase Order Endpoints

- **List all purchase orders:**

    ```http
    GET /api/purchase_orders/
    ```

- **Create a new purchase order:**

    ```http
    POST /api/purchase_orders/
    ```

- **Retrieve details of a specific purchase order:**

    ```http
    GET /api/purchase_orders/{po_id}/
    ```

- **Update a purchase order:**

    ```http
    PUT /api/purchase_orders/{po_id}/
    ```

- **Delete a purchase order:**

    ```http
    DELETE /api/purchase_orders/{po_id}/
    ```

- **Acknowledge a purchase order (update acknowledgment_date):**

    ```http
    POST /api/purchase_orders/{po_id}/acknowledge/
    ```

## Additional Notes

- Make sure to handle authentication and authorization according to your requirements.
- Update the models, views, and serializers as per your specific business logic.

Feel free to reach out if you have any questions or issues!
