booksList = ['abc', 'def', 'ghi']

class Library:
    def __init__(self, booksList):
        self.booksList = booksList

    def dispAvailableBooks(self):
        print('Available books:')
        for book in self.booksList:
            print(book)

    def lendBook(self, bookName):
        self.booksList.remove(bookName)

    def addBook(self, bookName):
        self.booksList.append(bookName)
        
        
class Customer:
    books = []
    def requestBook(self):
        print('Requested books name:')
        self.book = input()
        return self.book

    def returnBook(self, bookName):
        return bookName
    
    def addToCollection(self, bookName):
        Customer.books.append(bookName)
        print(bookName + ' added to the collection')

    def myCollection(self):
        print(Customer.books)
        return Customer.books


library = Library(booksList)
customer = Customer()

while True:
    print('------------------------------------------------------')
    print('Type 1 to display the available books\nType 2 to lend a book\nType 3 to return a book\nType 4 to check your collection')
    print('------------------------------------------------------')
    print('To EXIT the library write anything!')
    choose = input('Choose an option: ')
    print('------------------------------------------------------')
    match choose:
        case '1':
            library.dispAvailableBooks()
        case '2':
            book = input('Write the name of the book you want: ')
            library.lendBook(book)
            customer.addToCollection(book)
        case '3':
            book = input('Write the name of the book you want to return: ')
            if (book not in customer.myCollection()):
                print('You do not have this book')
            else:
                library.addBook(customer.returnBook(book))
        case '4':
            customer.myCollection()
        case _:
            break