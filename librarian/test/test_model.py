from librarian.models import Book, BookStatus, Loan, Member


def test_creation_book():
    my_book = Book(isbn="9780441172719", author = "Frank Herbert", title = "Dune", publication_year=1990, book_status=BookStatus.NOT_READY_FOR_RENT, id=None)

    assert my_book.isbn == "9780441172719"
    assert my_book.author == "Frank Herbert"
    assert my_book.title == "Dune"
    assert my_book.publication_year == 1990
    assert my_book.book_status == BookStatus.NOT_READY_FOR_RENT

def test_enumaration_book_status():
    assert BookStatus.AVAILABLE.value == "AVAILABLE"
    assert BookStatus.CHECKED_OUT.value == "CHECKED_OUT"
    assert BookStatus.LOST.value == "LOST"
    assert BookStatus.IN_REPAIR.value == "IN_REPAIR"
    assert BookStatus.NOT_READY_FOR_RENT.value == "NOT_READY_FOR_RENT"

def test_creation_member():
    my_member = Member(member_id=1, member_name="John Doe", email="john.doe@example.com", address="123 Main St")

    assert my_member.member_id == 1
    assert my_member.member_name == "John Doe"
    assert my_member.email == "john.doe@example.com"
    assert my_member.address == "123 Main St"
    assert my_member.fees == 0.0

def test_creation_loan():
    from datetime import datetime, timedelta

    borrow_date = datetime.now()
    due_date = borrow_date + timedelta(days=14)

    my_loan = Loan(book_id=1, member_id=1, loan_number=1, borrow_date=borrow_date, due_date=due_date)

    assert my_loan.book_id == 1
    assert my_loan.member_id == 1
    assert my_loan.loan_number == 1
    assert my_loan.borrow_date == borrow_date
    assert my_loan.due_date == due_date
    assert my_loan.returned_date is None
