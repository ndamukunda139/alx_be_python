# book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False  # Private attribute

    

class Library: 
    def __init__(self):
        self.__books = {}  # Private attribute   

    def add_book(self, book):
        self.__books[book.title] = book

    def check_out_book(self, title):
        if title in self.__books:
            book = self.__books[title]
            if not book._Book__is_checked_out:  # Accessing private attribute
                book._Book__is_checked_out = True
                return f"You have checked out '{title}'."
            else:
                return f"Sorry, '{title}' is already checked out."
        else:
            return f"Sorry, '{title}' is not available in the library."  
    
    def return_book(self, title):
        if title in self.__books:
            book = self.__books[title]
            if book._Book__is_checked_out:  # Accessing private attribute
                book._Book__is_checked_out = False
                return f"You have returned '{title}'."
            else:
                return f"'{title}' was not checked out."
        else:
            return f"Sorry, '{title}' does not belong to this library."
    
    def list_available_books(self):
        available_books = [title for title, book in self.__books.items() if not book._Book__is_checked_out]
        return available_books
    


