import csv
from datetime import date, timedelta
from models import Student, Book, BorrowRecord

class Library:
    def __init__(self, students=None, books=None):
        self.students = {s.student_id: s for s in (students or [])}
        self.books = {b.book_id: b for b in (books or [])}
        self.borrow_records = []

    def show_books(self):
        print("\n---------------- BOOK LIST ----------------")
        print(f"{'ID':<6} {'Title':<35} Available")
        print("-" * 55)
        for book in self.books.values():
            print(book)
        print("-" * 55)

    def search_book(self, book_id: str):
        return self.books.get(book_id)

    def borrow_book(self, student_id: str, book_id: str):
        if student_id not in self.students:
            raise ValueError("Student ID not found.")

        book = self.search_book(book_id)
        if book is None:
            raise ValueError("Book ID not found.")

        if book.available <= 0:
            raise ValueError("This book is out of stock.")

        # Prevent the same student from borrowing the same book twice.
        for record in self.borrow_records:
            if (
                record.student_id == student_id
                and record.book_id == book_id
                and record.status == "Borrowed"
            ):
                raise ValueError("This student already borrowed this book.")

        borrow_date = date.today()
        due_date = borrow_date + timedelta(days=14)

        book.borrow()

        record = BorrowRecord(
            student_id,
            book_id,
            borrow_date.isoformat(),
            due_date.isoformat(),
            "Borrowed",
        )
        self.borrow_records.append(record)

        print("\nBorrow successful.")
        print(f"Student: {self.students[student_id]}")
        print(f"Book: {book.title}")
        print(f"Borrow date: {borrow_date}")
        print(f"Due date: {due_date}")

    def return_book(self, student_id: str, book_id: str):
        record = self.find_active_record(student_id, book_id)

        if record is None:
            raise ValueError("Active borrow record not found.")

        today = date.today()
        due_date = date.fromisoformat(record.due_date)

        if today > due_date:
            overdue_days = (today - due_date).days
            print(f"Returned {overdue_days} day(s) late.")
        else:
            print("Returned on time.")

        book = self.search_book(book_id)
        if book is None:
            raise ValueError("Book ID not found.")

        book.return_book()
        record.status = "Returned"

        print(f"Return successful: {book.title}")

    def find_active_record(self, student_id: str, book_id: str):
        for record in self.borrow_records:
            if (
                record.student_id == student_id
                and record.book_id == book_id
                and record.status == "Borrowed"
            ):
                return record
        return None

    def check_overdue(self):
        today = date.today()
        found = False

        print("\n--------------- OVERDUE LIST ---------------")
        for record in self.borrow_records:
            if record.status != "Borrowed":
                continue

            due_date = date.fromisoformat(record.due_date)

            if today > due_date:
                overdue_days = (today - due_date).days
                print(
                    f"Student: {record.student_id} | "
                    f"Book: {record.book_id} | "
                    f"Due: {record.due_date} | "
                    f"Overdue: {overdue_days} day(s)"
                )
                found = True

        if not found:
            print("No overdue books.")
        print("---------------------------------------------")

    def show_borrow_records(self):
        print("\n--------------- BORROW RECORDS ---------------")
        if not self.borrow_records:
            print("No records.")
            return

        for record in self.borrow_records:
            print(
                f"Student: {record.student_id} | "
                f"Book: {record.book_id} | "
                f"Borrow: {record.borrow_date} | "
                f"Due: {record.due_date} | "
                f"Status: {record.status}"
            )

    def save_data(self, filename: str):
        try:
            with open(filename, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(
                    ["StudentID", "BookID", "BorrowDate", "DueDate", "Status"]
                )
                for record in self.borrow_records:
                    writer.writerow(record.to_list())
            print(f"Data saved to {filename}")
        except OSError as error:
            raise OSError(f"Cannot write file: {error}")

    def load_data(self, filename: str):
        try:
            with open(filename, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader, None)

                for row in reader:
                    if len(row) != 5:
                        continue

                    record = BorrowRecord.from_list(row)
                    self.borrow_records.append(record)

                    # Recalculate available copies from active records.
                    if record.status == "Borrowed":
                        book = self.search_book(record.book_id)
                        if book and book.available > 0:
                            book.available -= 1

        except FileNotFoundError:
            # First run: create a new empty data file.
            self.save_data(filename)
        except (OSError, csv.Error) as error:
            raise OSError(f"Cannot read data file: {error}")
