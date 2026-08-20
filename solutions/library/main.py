hand = set() 
book_set = set() 
 
class User: 
    pass
class Library:
    def book_list():
        global book_set
        print(*book_set, sep = ', ')
    def find_book(book):
        global book_set
        if book in book_set:
            print(book, 'found') 
        else:
            print(book, 'not found')    
class Book:
    def __init__(self, name_book):
        global book_set
        book_set.add(name_book)
        print('Book', name_book, 'added')
class Loan:
    def borrow_book(book):
        global hand
        global book_set
        if book in hand:
            print('you already have this book')
            return
        elif book not in book_set:
            print('there is no this book in library')
            return
        else:
            hand.add(book)
            print(book, 'successfully borrowed') 
        
    def return_book(book):
        global hand
        hand.discard(book)
        print(book, 'successfully returned') 





use = User()

library1=Library

while True:
    _ = input().split()
    
    
    if _[0] == 'list':
        library1.book_list()
    elif _[0] == 'add-book':
        book_ = Book(_[1])
    elif _[0] == 'borrow':
        Loan.borrow_book(_[1])
    elif _[0] == 'return':
        Loan.return_book(_[1])
    elif _[0] == 'find':
        library1.find_book(_[1])
    elif _[0] == 'help':
        print('nope')
    else:
        print('xz')
        
    
