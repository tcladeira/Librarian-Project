The Library - Project Structure

librarian/
│
├── src/
│   └── librarian/
│       ├── __init__.py
│       ├── models.py
│       ├── repository.py
│       ├── exceptions.py
│       │
│       └── adapters/
│           ├── __init__.py
│           └── memory.py
│
├── tests/
│   └── test_repository.py
│
├── docs/
│
├── examples/
│
├── pyproject.toml
├── README.md

Designing Models:

Member ---- Loan ---- Book

BOOK:
isbn -> string (unique)
author -> string
title -> string
id -> int (unique)
publication_year -> int
book_status -> BOOKSTATUS

BOOKSTATUS (ENUM):
available - 1
checked_out - 2
lost - 3
in_repair - 4

MEMBERS:
member_id -> int (unique)
member_name -> string
email -> string (unique)
fees -> float
address -> string

LOAN:
book_id -> int
member_id -> int
loan_number -> int (unique)
borrow_date -> datetime
due_date -> datetime
returned_date -> datetime | None
