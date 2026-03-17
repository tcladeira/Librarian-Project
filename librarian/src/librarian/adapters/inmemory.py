
from dataclasses import dataclass, field

from librarian.models import Book, Loan, Member


@dataclass
class InMemoryRepository:
    books: dict[int, Book] = field(default_factory=dict)
    members: dict[int, Member] = field(default_factory=dict)
    loans: dict[int, Loan] = field(default_factory=dict)

    def add_book(self, book: Book) -> None:
        if book.id in self.books:
            raise ValueError(f"Book with id {book.id} already exists.")
        self.books[book.id] = book

    def get_book_by_id(self, book_id: int) -> Book | None:
        return self.books.get(book_id)

    def list_books(self) -> dict[int, Book]:
        return self.books

    ##Member Operations##
    def add_member(self, member: Member) -> None:
        if member.member_id in self.members:
            raise ValueError(f"Member with id {member.member_id} already exists.")
        self.members[member.member_id] = member

    def get_member_by_id(self, member_id: int) -> Member | None:
        return self.members.get(member_id)

    def list_members(self) -> dict[int, Member]:
        return self.members

    ##Loan Operations## 
    def add_loan_by_id(self, loan: Loan) -> None:
        if loan.loan_id in self.loans:
            raise ValueError(f"Loan with id {loan.loan_id} already exists.")
        self.loans[loan.loan_id] = loan

    def get_loan_by_id(self, loan_id: int) -> Loan | None:
        return self.loans.get(loan_id)

    def list_loans(self) -> dict[int, Loan]:
        return self.loans


