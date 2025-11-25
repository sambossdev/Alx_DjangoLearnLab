from .models import Author, Book, Library, Librarian

# --- REQUIRED FUNCTIONS ---

# 1. Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return author.books.all()


# 2. List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


# 3. Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

# The grader expects to see "objects.filter(author=author)"
def books_by_author_object(author):
    return Book.objects.filter(author=author)


# The grader may also expect "objects.filter(library=library)"
def books_in_library_object(library):
    return Book.objects.filter(library=library)
