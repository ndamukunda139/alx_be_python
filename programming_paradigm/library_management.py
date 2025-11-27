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
        self.__books = {}  # Private attribute   

    def add_book(self, book):
        self.__books[book.title] = book
        return "{book.title} by {book.author}"

    def check_out_book(self, title):
        book = self.__books.get(title)
        if book:
            if book.check_out():
                return f"You have checked out '{title}'."
            else:
                return f"'{title}' is already checked out."
        else:
            return f"'{title}' not found in the library." 
    
    def return_book(self, title):
        book = self.__books.get(title)
        if book:
            if book.return_book():
                return f"You have returned '{title}'."
            else:
                return f"'{title}' was not checked out."
        else:
            return f"'{title}' not found in the library."
    
    def list_available_books(self):
        available_books = [title for title, book in self.__books.items() if not book._Book__is_checked_out]
        return available_books




