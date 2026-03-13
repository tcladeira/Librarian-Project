from librarian.adapters.inmemory import InMemoryRepository
from librarian.models import Book, Loan, Member


class RepositoryAPI:

    def __init__(self, repository: InMemoryRepository):
        self.repository = repository

    def add_book(self, book: Book) -> None:
        self.repository.add_book(book)

    def get_book_by_id(self, book_id: int) -> Book | None:
        return self.repository.get_book(book_id)

    def list_books(self) -> list[Book]:
        return self.repository.list_books()

    def add_member(self, member: Member) -> None:
        self.repository.add_member(member)

    def get_member_by_id(self, member_id: int) -> Member | None:
        return self.repository.get_member(member_id)

    def list_members(self) -> list[Member]:
        return self.repository.list_members()

    def add_loan(self, loan: Loan) -> None:
        self.repository.add_loan(loan)

    def get_loan_by_id(self, loan_id: int) -> Loan | None:
        return self.repository.get_loan(loan_id)

    def list_loans(self) -> list[Loan]:
        return self.repository.list_loans()