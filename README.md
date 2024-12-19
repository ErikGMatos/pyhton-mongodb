# Delivery Order Management System

This project is a Flask-based web application for managing delivery orders, providing CRUD operations and validation for order processing.

The Delivery Order Management System is designed to handle the creation, retrieval, updating, and deletion of delivery orders. It provides a robust backend infrastructure with a MongoDB database for data persistence, error handling mechanisms, and a well-structured codebase following best practices in software development.

Key features of the system include:
- RESTful API endpoints for order management
- MongoDB integration for data storage
- Custom error handling for various HTTP status codes
- Input validation for order creation and updates
- Modular architecture with clear separation of concerns

## Repository Structure

```
.
├── run.py
└── src
    ├── errors
    │   ├── error_handler.py
    │   └── types
    │       ├── http_bad_request_error.py
    │       ├── http_not_found_error.py
    │       └── http_unprocessable_entity_error.py
    ├── main
    │   ├── composer
    │   │   ├── registry_finder_composer.py
    │   │   ├── registry_order_composer.py
    │   │   └── registry_updater_composer.py
    │   ├── http_types
    │   │   ├── http_request.py
    │   │   └── http_response.py
    │   ├── routes
    │   │   └── delivery_routes.py
    │   └── server
    │       └── server.py
    └── models
        ├── connection
        │   └── connection_handler.py
        ├── repository
        │   ├── interfaces
        │   │   └── orders_repository.py
        │   ├── orders_repository.py
        │   └── orders_repository_test.py
        ├── usecases
        │   ├── registry_finder.py
        │   ├── registry_order.py
        │   └── registry_updater.py
        └── validators
            ├── registry_order_validator.py
            ├── registry_order_validator_test.py
            └── registry_updater_validator.py
```

Key Files:
- `run.py`: Entry point for the application
- `src/main/server/server.py`: Flask application setup
- `src/main/routes/delivery_routes.py`: API route definitions
- `src/models/connection/connection_handler.py`: Database connection management
- `src/models/repository/orders_repository.py`: Data access layer for orders
- `src/models/usecases/`: Business logic for order operations

## Usage Instructions

### Installation

Prerequisites:
- Python 3.7+
- MongoDB 4.4+

Steps:
1. Clone the repository:
   ```
   git clone <repository_url>
   cd delivery-order-management
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory with the following content:
   ```
   MONGODB_CONNECTION_STRING=<your_mongodb_connection_string>
   MONGODB_DATABASE_NAME=<your_database_name>
   ```

### Running the Application

To start the server:

```
python run.py
```

The server will start on `http://0.0.0.0:3000` in debug mode.

### API Endpoints

1. Create a new order:
   ```
   POST /delivery/order
   ```
   Request body example:
   ```json
   {
     "name": "John Doe",
     "address": "123 Main St",
     "cupom": false,
     "items": [
       {
         "item": "Pizza",
         "quantidade": 2
       }
     ]
   }
   ```

2. Get an order by ID:
   ```
   GET /delivery/order/<order_id>
   ```

3. Update an order:
   ```
   PATCH /delivery/order/<order_id>
   ```
   Request body example:
   ```json
   {
     "name": "Jane Doe",
     "address": "456 Elm St",
     "cupom": true
   }
   ```

### Testing

To run the tests:

```
pytest
```

Note: Some tests are currently skipped due to database interaction requirements.

### Troubleshooting

Common issues:

1. Database connection errors:
   - Ensure MongoDB is running and accessible
   - Check the connection string in the `.env` file
   - Verify network connectivity to the database server

2. Import errors:
   - Make sure you're running the application from the project root
   - Verify that all dependencies are installed correctly

3. API errors:
   - Check the request format and content against the API specifications
   - Look for detailed error messages in the server logs

For debugging:
- Set `debug=True` in `run.py` (already set by default)
- Check the console output for error messages and stack traces
- Use a tool like Postman to test API endpoints and examine responses

## Data Flow

The request data flow through the application follows these steps:

1. The client sends an HTTP request to one of the API endpoints.
2. The Flask server (`server.py`) receives the request and routes it to the appropriate handler in `delivery_routes.py`.
3. The route handler creates an `HttpRequest` object and passes it to the corresponding use case (e.g., `RegistryOrder`, `RegistryFinder`, or `RegistryUpdater`).
4. The use case validates the input using the appropriate validator (e.g., `registry_order_validator`).
5. If valid, the use case interacts with the `OrdersRepository` to perform the requested operation on the database.
6. The `OrdersRepository` uses the `DBConnectionHandler` to interact with the MongoDB database.
7. The result is then formatted into an `HttpResponse` object and returned to the client.

```
Client -> Flask Server -> Route Handler -> Use Case -> Validator
                                                    -> OrdersRepository -> DBConnectionHandler -> MongoDB
                                                    <- HttpResponse
       <- Flask Server <- Route Handler <- Use Case
```

Note: Error handling is performed at various stages, with custom error types being used to generate appropriate HTTP responses.