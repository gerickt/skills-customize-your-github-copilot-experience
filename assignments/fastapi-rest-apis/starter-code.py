from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    available: bool

books: List[Book] = [
    Book(id=1, title="1984", author="George Orwell", year=1949, available=True),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee", year=1960, available=True),
]

@app.get("/books", response_model=List[Book])
def list_books() -> List[Book]:
    return books

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", response_model=Book, status_code=201)
def create_book(book: Book) -> Book:
    if any(existing.id == book.id for existing in books):
        raise HTTPException(status_code=400, detail="Book with this ID already exists")
    books.append(book)
    return book

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book) -> Book:
    for index, book in enumerate(books):
        if book.id == book_id:
            if updated_book.id != book_id:
                raise HTTPException(status_code=400, detail="Book ID cannot be changed")
            books[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int) -> dict:
    for index, book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return {"detail": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
