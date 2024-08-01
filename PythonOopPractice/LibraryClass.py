booksList = ['abc', 'def', 'ghi']

class Library:
    def __init__(self, booksList):
        self.booksList = booksList

    def dispAvailableBooks(self):
        print('Available books:')
        for book in self.booksList:
            print(book)

    def lendBook(self, bookname):
        self.booksList.remove(bookname)

    def addBook(self, bookname):
        self.booksList.append(bookname)
        
class Customer:
    books = []
    def requestBook(self):
        print('Requested books name:')
        self.book = input()
        return self.book

    def returnBook(self):
        print('Returned books name:')
        self.book = input()
        return self.book
    
    def addToCollection(self, bookName):
        Customer.books.append(bookName)
        print(bookName + ' added to the collection')

    def myCollection(self):
        print(Customer.books)


library = Library(booksList)
customer = Customer()

while True:
    print('------------------------------------------------------')
    print('Type 1 to display the available books\nType 2 to lend a book\nType 3 to add a book\nType 4 to return a book\nType 5 to check your collection')
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
            book = input('Write the name of the book you want to add: ')
            #any book can be added
        case '4':
            book = input('Write the name of the book you want to return: ')
            #the book name has to be in the collection
        case '5':
            customer.myCollection()
        case _:
            break