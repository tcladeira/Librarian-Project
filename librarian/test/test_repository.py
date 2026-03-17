from datetime import datetime, timedelta

from librarian.adapters.inmemory import InMemoryRepository
from librarian.models import Book, BookStatus, Loan, Member
from librarian.repository import RepositoryAPI


def test_bookapi_add_book():
    repo = InMemoryRepository()
    book = Book(isbn="9780441172719", author = "Frank Herbert", title = "Dune", publication_year=1990, book_status=BookStatus.NOT_READY_FOR_RENT, id=1)
    member = Member(member_id=1, member_name="John Doe", email="someemail@gmail.com", address="Some address")
    api = RepositoryAPI(repo)
    api.add_book(book)
    retrieved_book = api.get_book_by_id(book.id)
##Test Book Operations using API##
    assert retrieved_book == book
    assert list(api.list_books().values()) == [book]

def test_memberapi_add_member():
    repo = InMemoryRepository()
    member = Member(member_id=1, member_name="John Doe", email="someemail@gmail.com", address="Some address")
    api = RepositoryAPI(repo)
    api.add_member(member)
    retrieved_member = api.get_member_by_id(member.member_id)
##Test Member Operations using API##
    assert retrieved_member == member
    assert list(api.list_members().values()) == [member]

def test_loanapi_add_loan():
    repo = InMemoryRepository()
    book = Book(isbn="9780441172719", author = "Frank Herbert", title = "Dune", publication_year=1990, book_status=BookStatus.NOT_READY_FOR_RENT, id=1)
    member = Member(member_id=1, member_name="John Doe", email="someemail@gmail.com", address="Some address")
    loan = Loan(loan_id=1, book_id=1, member_id=1, borrow_date=datetime.now(), due_date=datetime.now() + timedelta(days=14))
    api = RepositoryAPI(repo)
    api.add_loan_by_id(loan)
    retrieved_loan = api.get_loan_by_id(loan.loan_id)
##Test Loan Operations using API##
    assert retrieved_loan == loan
    assert list(api.list_loans().values()) == [loan]

