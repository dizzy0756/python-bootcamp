class Book:

    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def borrow(self):
        self.is_borrowed = True
    
    def return_book(self):
        self.is_borrowed = False
    
    def display(self):
        print(f"'{self.title}' by {self.author}")
        if self.is_borrowed == True:
            print("Status : Not available")
        else:
            print("Status : Available")


class Ebook(Book):
    def __init__(self, title, author,file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def display(self):
        super().display()
        print(f"Size : {self.file_size}")
    
class Library():
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            book.display()


library = Library()
while True:
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Show Books")
    print("5. Exit")

    while True:
        try:
            choice = int(input("Enter your choice : "))
            break
        except ValueError:
            print("Enter a valid number from the menu")
    
    if choice == 5:
        break

    match choice:
        case 1:
            title = input("Enter the title of the book : ")
            author = input("Enter the name of the author : ")
            is_ebook = input("Is your book an e-book [Y/N] : ")
            if is_ebook.lower() == "y":
                file_size = int(input("Enter the size of the Ebook: "))
                book = Ebook(title,author,file_size)
            else:    
                book = Book(title,author)
            
            library.add_book(book)

        case 2:
            title = input("Enter the title of the book you want to borrow")
            found = False
            for item in library.books:
                if item.title == title:
                    found = True
                    if item.is_borrowed == True:
                        print("Book is borrowed by someone else")
                    else:
                        item.borrow()
            if found == False:
                print(f"Book with the title '{title}' does not exist in the library")
        case 3:
            title = input("Enter the title of the book you want to return")
            found = False
            for item in library.books:
                if item.title == title:
                    found = True
                    if item.is_borrowed == True:
                        item.return_book()
                    else:
                        print(f"Cannot return the book. '{title}' was not borrowed by anyone.")
            if found == False:
                print(f"Book with the title '{title}' does not exist in the library")
            
        case 4:
            library.display_books()

        case _:
            print("Invalid Choice")