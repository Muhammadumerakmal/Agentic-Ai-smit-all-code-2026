class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed  # Finishing your line here

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_available_books(self):
        print("Available Books:")
        # We loop through the list of book objects
        for book in self.books:
            # We check the 'is_borrowed' attribute of each object
            if not book.is_borrowed:
                print(f"- {book.title} by {book.author}")

# --- Test your system ---
my_library = Library()

# Create books
b1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
b2 = Book("1984", "George Orwell")
b3 = Book("The Hobbit", "J.R.R. Tolkien")

# Add to library
my_library.add_book(b1)
my_library.add_book(b2)
my_library.add_book(b3)

# Borrow one
b2.is_borrowed = True

# Show only available
my_library.show_available_books()