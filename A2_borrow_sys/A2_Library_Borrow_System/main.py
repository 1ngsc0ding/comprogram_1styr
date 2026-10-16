from models import Student, Book, BorrowRecord
from library import Library


def create_library():
    """Create sample library data."""
    students = [
        Student("690101", "Chonpatchut Boonpalit"),
        Student("690102", "Anan Suksan"),
        Student("690103", "Somsak Jaidee"),
    ]

    # 2D array: [book_id, title, total_quantity]
    book_data = [
        ["B001", "Python Programming", 3],
        ["B002", "Data Structure", 2],
        ["B003", "Computer Network", 4],
        ["B004", "Database System", 2],
        ["B005", "Object Oriented Programming", 1],
    ]

    books = [Book(row[0], row[1], row[2]) for row in book_data]
    return Library(students, books)


def show_menu():
    print("\n========== UNIVERSITY LIBRARY ==========")
    print("1. Show books")
    print("2. Search book")
    print("3. Borrow book")
    print("4. Return book")
    print("5. Check overdue")
    print("6. Show borrow records")
    print("7. Save data")
    print("0. Exit")
    print("========================================")


def main():
    library = create_library()
    library.load_data("data/borrow_records.csv")

    while True:
        show_menu()
        choice = input("Select menu: ").strip()

        try:
            if choice == "1":
                library.show_books()

            elif choice == "2":
                book_id = input("Enter book ID: ").strip()
                book = library.search_book(book_id)
                if book:
                    print(
                        f"Found: {book.book_id} | {book.title} | "
                        f"Available: {book.available}/{book.total_quantity}"
                    )
                else:
                    print("Book not found.")

            elif choice == "3":
                student_id = input("Enter student ID: ").strip()
                book_id = input("Enter book ID: ").strip()
                library.borrow_book(student_id, book_id)

            elif choice == "4":
                student_id = input("Enter student ID: ").strip()
                book_id = input("Enter book ID: ").strip()
                library.return_book(student_id, book_id)

            elif choice == "5":
                library.check_overdue()

            elif choice == "6":
                library.show_borrow_records()

            elif choice == "7":
                library.save_data("data/borrow_records.csv")

            elif choice == "0":
                library.save_data("data/borrow_records.csv")
                print("Program ended.")
                break

            else:
                print("Invalid menu. Please select 0-7.")

        except ValueError as error:
            print(f"Input error: {error}")
        except FileNotFoundError as error:
            print(f"File error: {error}")
        except Exception as error:
            print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
