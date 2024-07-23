from fastapi import FastAPI, Body

app = FastAPI()


BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "Science"},
    {"title": "Title Two", "author": "Author Two", "category": "Science"},
    {"title": "Title Three", "author": "Author Three", "category": "History"},
    {"title": "Title Four", "author": "Author Four", "category": "Geography"},
    {"title": "Title Five", "author": "Author Five", "category": "English"},
]



@app.get("/")
async def first_api():
    return {"message": "Hello World!"}

@app.get("/books")
def get_all_books():
    return BOOKS


# # Static variable
# @app.get("/books/my_book")
# async def read_all_books():
#     return  {'book_title' : 'My Favorite book'}


# # Dynamic Parameter
# @app.get("/books/{dynamic_param}")
# async def read_all_books(dynamic_param:str):
#     return {"dynamic_param" : dynamic_param}



# Query parameter solution
@app.get("/books/by_author/")
async def read_books_by_author_query_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book


# To filter data based on provided url we use Query Parameter


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (
            book.get("author").casefold() == book_author.casefold()
            and book.get("category").casefold() == category.casefold()
        ):
            books_to_return.append(book)
    return books_to_return




@app.post("/books/create_book")
async def create_book(new_book = Body()):
    BOOKS.append(new_book)



@app.put("/books/update_book")
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book



@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break


# 1. Create a new API Endpoint that can fetch all books from a specific author using either Path Parameters or Query Parameters.


# path parameter solution
@app.get("/books/by_author/{author}")
async def read_books_by_author_param_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return


# # Query parameter solution
# @app.get("/books/by_author/")
# async def read_books_by_author_query_path(author: str):
#     books_to_return = []
#     for book in BOOKS:
#         if book.get('author').casefold() == author.casefold():
#             books_to_return.append(book)
#     return books_to_return