# CLI Library

Your task is to create a CLI Library, where you can `add-book`'s to the library, `list` all available books, `borrow` some `<book>`, `return` this `book`, and `find <book>` in the library.

## Requirements

- All data MUST be stored in MEMORY, no persistance allowed on  the first stage.
- There MUST be at least 4 Entities (python class):
-- Book
-- User
-- Library
-- Loan

## Minimum CLI commands

```
list          # - list all books in library
add-book      # - add book to library
borrow <book> # - borrow book from library
return <book> # - return previously borrowed book
find <book>   # - check whatever the book is in library or not
```

## Run

```bash
python3 main.py
# Library cli opened
library> add-book book1
Book book1 added
library> add-book book2
Book book2 added
library> list
book1, book2
library> borrow book1
book1 successfully borrowed
library> return book1
book1 successfully returned
library> find book3
book3 not found
library> find book1
book1 found
```

## UPDATE 21.08.26

1. Save data to json file so program can survive restart
2. Several users may borrow books
3. Several books with same name
4. User may borrow no more than 3 books
5. Books import/export
6. Split program into modules
