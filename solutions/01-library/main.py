from dataclasses import dataclass
import json
from models.user import User
from library import Library, library1
from models.loan import Loan
from models.book import Book

library1.save_load()
        
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
        print('book', input_text[1], 'added')
        
    elif input_text[0] == 'borrow':
        if len(input_text) != 2:
            print('usage: borrow <book_name>')
            continue
        library1.borrow_book(input('on who register book? '), input_text[1])
    elif input_text[0] == 'return':
        if len(input_text) != 2:
            print('usage: return <book_name>')
            continue
        library1.return_book(input('on who register book? '), input_text[1])
    elif input_text[0] == 'find':
        if len(input_text) != 2:
            print('usage: find <book_name>')
            continue
        library1.find_book(input_text[1])
    elif input_text[0] == 'exit':
        print('bye bye')
        library1.save_data()
        break
    elif input_text[0] == 'import':
        if len(input_text) != 2:
            print('usage: import <file_name>')
            continue        
        library1.import_books(input_text[1])
    elif input_text[0] == 'export':
        if len(input_text) != 2:
            print('usage: export <file_name>')
            continue        
        library1.export_books(input_text[1])   
    elif input_text[0] == 'help':
        print('''
        list: see all books in the library
        add-book <book name>: add book to the library
        borrow <book name>: borrow book from the library
        return <book name>: return book to the library
        find <book name>: check if book is in the library
        import <file name>: import books from file to the library
        export <file name>: export books to file from the library 
        exit: end of program
        ''')    
    else:
        print('unknown command')
    library1.save_data()
    
        
    
