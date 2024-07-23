from typing import Optional
from fastapi import FastAPI, Body, HTTPException, Path, Query
from pydantic import BaseModel, Field
from starlette import status

# Field will allow us to be able to add validation to each field of that request object


app = FastAPI()


# Creating a new book object
# Truth
class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    # creating a constructor
    # __init__ is to initialization of our constructor
    # self is a refrence to our class of Book
    def __init__(self, id, title, author, description, rating, published_date):
        # Now assign our Book variables to our constructor that we are passing in
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date= published_date



# new object 
# Truthful
class BookRequest(BaseModel):
    id: Optional[int] = Field(description='id is not needed on create', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2031)
    
# None: it could be either int type or None(null)


# For a specific Example Values to the swagger
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "tybans",
                "description": "A new description of a book",
                "rating": 5,
                "published_date": 2029
            }
        }
    }




BOOKS = [
    Book(1, "Python", "tybans", "A very useful book", 5, 2030),
    Book(2, "Java", "Ansari", "A useful book", 4, 2012),
    Book(3, "C++", "Taiyab", "A great book", 3, 2015),
    Book(4, "JavaScript", "Snehal", "An awesome book", 5, 2022),
    Book(5, "FastAPI", "Sanjoy", "A very useful book", 3, 2024),
    Book(6, "HTML", "Abhishek", "A lovely book", 5, 2026),
]


@app.get("/")
async def first_endpoint():
    return {"message": "server is running..."}


@app.get("/books", status_code= status.HTTP_200_OK)
async def get_all_books():
    return BOOKS


# fetch single book using path parameter
# Path: adding extra validation to path parameters
@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def get_book_by_id(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book

    
    raise HTTPException(status_code=404, detail='Item not found')



# Filter by rating using query parameter
# Query: adding extra validation to query parameter
@app.get("/books/", status_code=status.HTTP_200_OK)
async def get_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return



@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def get_book_by_publish_date(published_date: int = Query(gt=1999, lt=2031)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return



# @app.post("/create_book")
# async def create_book(book_request=Body()):
#     BOOKS.append(book_request)
    
# Using Body, does not add any kind of Validation into our application

# We will be implementing pydantics for data validation
@app.post("/create_book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request:BookRequest):
    new_book = Book(**book_request.model_dump())
    print(type(new_book))
    BOOKS.append(find_book_id(new_book))



# just a normal python function
def find_book_id(book: Book):
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1

    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
 
    return book



@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')







# Assignment

# Here is your opportunity to keep learning!

# Add a new field to Book and BookRequest called published_date: int (for example, published_date: int = 2012). So, this book as published on the year of 2012.

# Enhance each Book to now have a published_date

# Then create a new GET Request method to filter by published_date