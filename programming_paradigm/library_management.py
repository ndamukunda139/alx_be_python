# book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False  # Private attribute
    
    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False
    

class Library(): 
    def __init__(self):
        self.__books = []  # Private attribute   

    def add_book(self, book):
        books = self.__books.append(book)
        return books
    
    def check_out_book(self, title):
        books = self.__books.remove(book for book in self.__books if book.title == title and not book._Book__is_checked_out)
        return books
    
    def return_book(self, title):
        books = self.__books.append(book for book in self.__books if book.title == title and book._Book__is_checked_out)
        return books
    
    def list_available_books(self):
        available_books = [book.title for book in self.__books if not book._Book__is_checked_out]
        return available_books
        

