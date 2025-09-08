class Library:
    def __init__(self,name):
        self.name=name
        self.books=[]

    def add_book(self,book):
        self.books.append(book)

    def books_list(self):
        return(f"{book.title} by {book.author}"for book in self.books)
    
class Book:
    def __init__(self,title,author):
        self.author=author
        self.title=title

lib=Library("Anna Centenary")

no_of_books=int(input("Enter the number of books your wanna add: "))

for i in range(1,no_of_books+1):
    title = input(f"Enter the title of book {i}: ")
    author = input(f"Enter the author of book {i}: ")
    book = Book(title, author)
    lib.add_book(book)

print(lib.name)

for book in lib.books_list():
    print(book)