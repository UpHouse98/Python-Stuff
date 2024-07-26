booksList = ['abc', 'def', 'ghi']

class Library:
    def __init__(self, booksList) -> None:
        self.booksList = booksList

    def dispAvailableBooks(self):
        for book in self.booksList:
            print(book)

    def lendBook(self, bookName):
        self.booksList.remove(bookName)

    def addBook(self, bookName):
        self.booksList.append(bookName)
        


class Customer:
    def requestBook(self):
        print('Enter the name of the book you want:')
        self.book = input()
        return self.book

    def returnBook():
        pass


library = Library(booksList)
customer = Customer()

library.dispAvailableBooks()