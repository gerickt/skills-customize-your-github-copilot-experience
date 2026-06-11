# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Practice building a RESTful API using FastAPI by defining routes, request models, and CRUD operations for a simple resource.

## 📝 Tasks

### 🛠️ Build the API Structure

#### Description
Create a FastAPI application that manages a collection of books. Define a Pydantic model for the book data and set up the app instance with the required routes.

#### Requirements
Completed program should:

- Use `FastAPI` and `Pydantic` for request handling and validation.
- Define a `Book` model with fields for `id`, `title`, `author`, `year`, and `available`.
- Store book records in an in-memory list.
- Expose the app via `app = FastAPI()`.

### 🛠️ Create CRUD Endpoints

#### Description
Implement the main RESTful endpoints for listing books, retrieving a single book, creating a new book, updating an existing book, and deleting a book.

#### Requirements
Completed program should:

- Provide `GET /books` to return all books.
- Provide `GET /books/{book_id}` to return a single book by ID.
- Provide `POST /books` to add a new book.
- Provide `PUT /books/{book_id}` to update an existing book.
- Provide `DELETE /books/{book_id}` to remove a book.
- Return appropriate HTTP status codes for success, not found, and validation errors.

### 🛠️ Validate Input and Handle Errors

#### Description
Add request validation and error handling so the API responds cleanly when users send invalid data or request missing resources.

#### Requirements
Completed program should:

- Validate incoming book payloads using Pydantic.
- Return `404 Not Found` when a book ID does not exist.
- Return `400 Bad Request` when attempting to create a book with a duplicate ID.
- Use meaningful error messages in the response.
