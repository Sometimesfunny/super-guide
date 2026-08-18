hand = set() # #pfdnf ljltkf.
book_set = set() 

class User: #exist
    pass
class Library: # list 
    pass
class Book: #find add
    pass
class Loan: #borrow return
    pass

def book_list():
    global book_set
    print(book_set, 'натъ') #
    
def add_book(book):
    global book_set
    book_set.add(book)
    print('added') #
    
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
        print('boroved') #

def return_book(book):
    global hand
    hand.discard(book)
    print('returned') #
    
    
def find_book(book):
    global book_set
    if book in book_set:
        print('yest') #
    else:
        print('')






while True:
    _ = input().split()
    
    
    if _[0] == 'list':
        book_list()
    elif _[0] == 'add-book':
        add_book(_[1])
    elif _[0] == 'borrow':
        borrow_book(_[1])
    elif _[0] == 'return':
        return_book(_[1])
    elif _[0] == 'find':
        find_book(_[1])
    elif _[0] == 'help':
        print('nope')
    else:
        print('xz')
        
    