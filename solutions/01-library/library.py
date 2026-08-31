import json
from book import Book
from loan import Loan

class Library:
    
    def __init__(self):
        self.book_list_: list[Book] = list()
        self.loans: set[Loan] = set()

    def save_data(self):
        
        with open('library.json', 'w',) as json_file:
            json.dump({'books' : [x.name for x in self.book_list_], 'loans' : [{x.name : x.book_name} for x in self.loans]}, json_file)
     
    def save_load(self):
        try:
            with open('library.json', 'r') as json_file:
                data = json.load(json_file)
                    
                for i in data.get('books'):
                    book_ = Book(i)
                    library1.add_book(book_)
                    
                    for i in data.get('loans'):
                        for name, book_name in i.items():
                            loan = Loan(
                                name= name,
                                book_name= book_name
                            )   
                            library1.add_loan(loan)
        except FileNotFoundError:
            print("<no save was found>")         
         
    def book_list(self):
        print(self.book_list_)

    def find_book(self, book_name: str):
        if book_name in [x.name for x in self.book_list_]:
            print(book_name, 'found') 
        else:
            print(book_name, 'not found')

    def add_book(self, book: Book):
        self.book_list_.append(book)
        
    def borrow_book(self, name: str, book_name: str):
        if book_name not in [x.name for x in self.book_list_]:
            print('there is no this book in library')
            return
        loan_per_name = 0
        for i in [x for x in self.loans]:
            if i.name == name:
                loan_per_name += 1
        if loan_per_name >= 3:
            print('you may not borrow more than 3 books')
            return
        
        new_loan = Loan(
            name=name,
            book_name=book_name
            )
        self.loans.add(new_loan)
        for i in self.book_list_:
            if i.name == book_name:
                self.book_list_.remove(i)
                break
        print(book_name, 'successfully borrowed') 
        
    def return_book(self, name: str, book_name: str):
        global library1
        loan_to_remove = None
        for loan in self.loans:
            if loan.name == name and loan.book_name == book_name:
                loan_to_remove = loan
                break
        else:
            print('no loan for this name and book found')
            return
        self.loans.remove(loan_to_remove)
        book_ = Book(book_name)
        library1.add_book(book_)
        print(book_name, 'successfully returned') 
    
    def add_loan(self, loan):
        self.loans.add(loan)
    
    def import_books(self, file):
        try:
            with open(file, 'r') as f:
                for i in f.read().split(' ,'):
                    book_ = Book(i)
                    library1.add_book(book_)            
                    print('import successfully')
        except FileNotFoundError:
            print('File not found')
    def export_books(self, file):
        with open(file, 'w') as f:
            f.write(' ,'.join([x.name for x in self.book_list_]))   
            print('export successfully')


            
library1=Library()

