# A2 Function Design

## 1. `create_library()`
- Parameters: None
- Return: `Library`
- Purpose: Create sample Student and Book objects and return a Library object.

## 2. `show_menu()`
- Parameters: None
- Return: `None`
- Purpose: Display the main menu.

## 3. `main()`
- Parameters: None
- Return: `None`
- Purpose: Control the program and receive user menu choices.

## 4. `Library.show_books()`
- Parameters: None
- Return: `None`
- Purpose: Display all books and available quantities.

## 5. `Library.search_book(book_id: str)`
- Parameters: `book_id: str`
- Return: `Book | None`
- Purpose: Search for a book by its ID.

## 6. `Library.borrow_book(student_id: str, book_id: str)`
- Parameters: `student_id: str`, `book_id: str`
- Return: `None`
- Purpose: Validate student/book, check quantity, create a borrow record, set due date to 14 days, and reduce available quantity.

## 7. `Library.return_book(student_id: str, book_id: str)`
- Parameters: `student_id: str`, `book_id: str`
- Return: `None`
- Purpose: Find the active record, calculate overdue days, update status, and increase available quantity.

## 8. `Library.check_overdue()`
- Parameters: None
- Return: `None`
- Purpose: Find active records whose due date has passed.

## 9. `Library.find_active_record(student_id: str, book_id: str)`
- Parameters: `student_id: str`, `book_id: str`
- Return: `BorrowRecord | None`
- Purpose: Find an active borrow record.

## 10. `Library.save_data(filename: str)`
- Parameters: `filename: str`
- Return: `None`
- Purpose: Write borrow records to a CSV file.

## 11. `Library.load_data(filename: str)`
- Parameters: `filename: str`
- Return: `None`
- Purpose: Read borrow records from a CSV file and restore active book quantities.
