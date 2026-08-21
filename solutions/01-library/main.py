# FIX: we can return book twice
# FIX: no empty input allowed
# FIX: No library> input string
# TODO: Help

from dataclasses import dataclass

@dataclass(unsafe_hash=True)
class User: 
    name: str

class Library:
    def __init__(self):
        self.book_set: set[Book] = set()
        self.loans: set[Loan] = set()

    def book_list(self):
        print(*self.book_set, sep = ', ')

    def find_book(self, book_name: str):
        if book_name in [x.name for x in self.book_set]:
            print(book_name, 'found') 
        else:
            print(book_name, 'not found')

    def add_book(self, book: Book):
        self.book_set.add(book)
        print('Book', book.name, 'added')

    def borrow_book(self, name: str, book_name: str):
        if book_name in [x.book_name for x in self.loans]:
            print('someone already have this book')
            return
        elif book_name not in [x.name for x in self.book_set]:
            print('there is no this book in library')
            return
        else:
            new_loan = Loan(
                name=name,
                book_name=book_name
            )
            self.loans.add(new_loan)
            print(book_name, 'successfully borrowed') 
        
    def return_book(self, name: str, book_name: str):
        loan_to_remove = None
        for loan in self.loans:
            if loan.name == name and loan.book_name == book_name:
                loan_to_remove = loan
                break
        else:
            print('no loan for this name and book found')
            return
        self.loans.remove(loan_to_remove)
        print(book_name, 'successfully returned') 

@dataclass(unsafe_hash=True)
class Book:
    name: str

@dataclass(unsafe_hash=True)
class Loan:
    name: str
    book_name: str

use = User('ivan')

library1=Library()

while True:
    input_text = input('library> ').split()
    if len(input_text) == 0:
        continue
    if input_text[0] == 'list':
        library1.book_list()
    elif input_text[0] == 'add-book':
        if len(input_text) != 2:
            print('usage: add-book <book_name>')
            continue
        book_ = Book(input_text[1])
        library1.add_book(book_)
    elif input_text[0] == 'borrow':
        if len(input_text) != 2:
            print('usage: borrow <book_name>')
            continue
        library1.borrow_book(use.name, input_text[1])
    elif input_text[0] == 'return':
        if len(input_text) != 2:
            print('usage: return <book_name>')
            continue
        library1.return_book(use.name, input_text[1])
    elif input_text[0] == 'find':
        if len(input_text) != 2:
            print('usage: find <book_name>')
            continue
        library1.find_book(input_text[1])
    elif input_text[0] == 'help':
        print('nope')
    elif input_text[0] == 'exit':
        print('bye bye')
        break
    else:
        print('unknown command')
        
    
