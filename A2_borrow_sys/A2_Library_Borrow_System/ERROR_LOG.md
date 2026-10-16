# A2 Error Log

## Error 1: FileNotFoundError
**Cause:** The data file does not exist on the first run.

**How it was fixed:** Use `try-except FileNotFoundError` in `load_data()`. If the file does not exist, the program creates a new CSV file.

---

## Error 2: ValueError - Student ID not found
**Cause:** The user enters a student ID that is not stored in the system.

**How it was fixed:** Check `student_id in self.students` before creating a borrow record.

---

## Error 3: ValueError - Book ID not found
**Cause:** The user enters a book ID that does not exist.

**How it was fixed:** Use `search_book()` and check whether the returned value is `None`.

---

## Error 4: ValueError - Book out of stock
**Cause:** The available quantity of the selected book is 0.

**How it was fixed:** Check `book.available <= 0` before borrowing.

---

## Error 5: Duplicate active borrowing
**Cause:** A student tries to borrow the same book again before returning it.

**How it was fixed:** Search active borrow records before creating a new record.

---

## Error 6: ValueError - Invalid return record
**Cause:** A student tries to return a book that they do not currently have borrowed.

**How it was fixed:** Use `find_active_record()` and stop the return operation when no record is found.

---

## Error 7: OSError while reading/writing files
**Cause:** The operating system may reject file access.

**How it was fixed:** Wrap file operations with `try-except` and show a readable error message.

---

## Demo test cases

### Test 1: Normal borrow
Input:
- Student ID: `690101`
- Book ID: `B001`

Expected:
- Borrow successful
- Available quantity decreases by 1
- Due date is 14 days after borrow date

### Test 2: Invalid student
Input:
- Student ID: `999999`
- Book ID: `B001`

Expected:
- `Student ID not found.`

### Test 3: Invalid book
Input:
- Student ID: `690101`
- Book ID: `B999`

Expected:
- `Book ID not found.`

### Test 4: Out of stock
Set a book's available quantity to 0 and try to borrow it.

Expected:
- `This book is out of stock.`

### Test 5: Return
Input:
- Student ID: `690101`
- Book ID: `B001`

Expected:
- Return successful
- Available quantity increases by 1

### Test 6: Overdue
Create or edit a record so that the due date is before today's date.

Expected:
- Program displays the number of overdue days.
