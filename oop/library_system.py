class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title, author, file_size: int):
        self.file_size = file_size
        super().__init__(title, author)


class PrintBook(Book):
    def __init__(self, title, author, page_count: int):
        self.page_count = page_count
        super().__init__(title, author)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(
                    f"Ebook: {book.title} by {book.author} File Size:{book.file_size}")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author} Page Count:{book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")
