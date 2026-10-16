class Student:
    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = name

    def __str__(self):
        return f"{self.student_id} - {self.name}"

class Book:
    def __init__(self, book_id: str, title: str, total_quantity: int):
        self.book_id = book_id
        self.title = title
        self.total_quantity = total_quantity
        self.available = total_quantity

    def borrow(self):
        if self.available <= 0:
            raise ValueError("This book is out of stock.")
        self.available -= 1

    def return_book(self):
        if self.available >= self.total_quantity:
            raise ValueError("All copies of this book are already in the library.")
        self.available += 1

    def __str__(self):
        return (
            f"{self.book_id:<6} {self.title:<35} "
            f"{self.available}/{self.total_quantity}")

class BorrowRecord:
    def __init__(self, student_id: str, book_id: str, borrow_date: str, due_date: str, status: str = "Borrowed",):
        self.student_id = student_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.status = status

    def to_list(self):
        return [self.student_id, self.book_id, self.borrow_date, self.due_date, self.status]

    @classmethod
    def from_list(cls, row):
        return cls(row[0], row[1], row[2], row[3], row[4])
