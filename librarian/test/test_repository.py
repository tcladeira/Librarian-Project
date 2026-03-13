from datetime import datetime, timedelta

from librarian.adapters.inmemory import (
    InMemoryBookRepository,
    InMemoryLoanRepository,
    InMemoryMemberRepository,
)
from librarian.models import Book, BookStatus, Loan, Member


def test_book_repository():
    repo = InMemoryBookRepository()
    book = Book(isbn="9780441172719", author = "Frank Herbert", title = "Dune", publication_year=1990, book_status=BookStatus.NOT_READY_FOR_RENT, id=None)
    member = Member(member_id=1, member_name="John Doe", email="someemail@gmail.com", address="Some address")
    repo.add_book(book)
    repo.add_member(member)    

    ##Test if the book was added correctly to the repository##
    assert len(repo.books) == 1
    assert repo.books[0].isbn == "9780441172719"
    assert repo.books[0].author == "Frank Herbert"
    assert repo.books[0].title == "Dune"
    assert repo.books[0].publication_year == 1990
    assert repo.books[0].book_status == BookStatus.NOT_READY_FOR_RENT

def test_add_member_repository():
    repo = InMemoryMemberRepository()
    member = Member(member_id=1, member_name="John Doe", email="someemail@gmail.com", address="Some address")
    repo.add_member(member)


def test_add_loan_repository():
    repo = InMemoryLoanRepository()
    fix_date = datetime(2024, 1, 1)
    loan = Loan(book_id=1, member_id=1, loan_number=1, borrow_date=fix_date, due_date=fix_date + timedelta(days=14), returned_date=None)
    repo.add_loan(loan)

    ##Test if the loan was added correctly to the repository##
    assert len(repo.loans) == 1
    assert repo.loans[0].book_id == 1
    assert repo.loans[0].member_id == 1
    assert repo.loans[0].loan_number == 1
    assert repo.loans[0].borrow_date == fix_date
    assert repo.loans[0].due_date == fix_date + timedelta(days=14)
    assert repo.loans[0].returned_date is None

def test_retrieving_book_from_repository():
    repo = InMemoryBookRepository()
    book = Book(isbn="9780441172719", author = "Frank Herbert", title = "Dune", publication_year=1990, book_status=BookStatus.NOT_READY_FOR_RENT, id=None)
    repo.add_book(book)

    ##Test if we can retrieve the book from the repository##
    retrieved_book = repo.books[0]
    assert retrieved_book.isbn == "9780441172719"
    assert retrieved_book.author == "Frank Herbert"
    assert retrieved_book.title == "Dune"
    assert retrieved_book.publication_year == 1990
    assert retrieved_book.book_status == BookStatus.NOT_READY_FOR_RENT

def test_listing_books_from_repository():
    repo = InMemoryBookRepository()
    book1 = Book(isbn="9780441172719", author = "Frank Herbert", title = "Dune", publication_year=1990, book_status=BookStatus.NOT_READY_FOR_RENT, id=None)
    book2 = Book(isbn="9780553386790", author = "George R. R. Martin", title = "A Game of Thrones", publication_year=1996, book_status=BookStatus.AVAILABLE, id=None)
    repo.add_book(book1)
    repo.add_book(book2)

    ##Test if we can list all the books from the repository##
    assert len(repo.books) == 2
    assert repo.books[0].isbn == "9780441172719"
    assert repo.books[1].isbn == "9780553386790"
