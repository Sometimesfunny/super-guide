from dataclasses import dataclass

@dataclass(unsafe_hash=True)
class Loan:
    name: str
    book_name: str

