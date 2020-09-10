from bookManager.models import Book
from .TestAuthor import TestAuthor

class TestBook:
    isbn="23456534-1"
    title="Der Herr der Rine"
    read = False
    test_author = TestAuthor()

    def __init__(self):
        try:
            Book.objects.get(title=self.title)
        except Book.DoesNotExist:

            book = Book.objects.create(
                isbn=self.isbn,
                title=self.title,
                read=self.read
            )
            book.authors.add(self.test_author.get_test_author())

    def get_test_book(self):
        return Book.objects.get(title=self.title)