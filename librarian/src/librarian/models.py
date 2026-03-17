from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class BookStatus(Enum):
    AVAILABLE = "AVAILABLE"
    CHECKED_OUT = "CHECKED_OUT"
    LOST = "LOST"
    IN_REPAIR = "IN_REPAIR"
    NOT_READY_FOR_RENT = "NOT_READY_FOR_RENT"

@dataclass
class Book:
    isbn: str
    author: str
    title: str
    id: int | None
    publication_year: int
    book_status: BookStatus

@dataclass
class Member:
    member_id: int | None
    member_name: str
    email: str
    address: str
    fees: float = 0.0

@dataclass
class Loan:
    book_id: int
    member_id: int
    loan_id: int 
    borrow_date: datetime
    due_date: datetime
    returned_date: datetime | None = None
