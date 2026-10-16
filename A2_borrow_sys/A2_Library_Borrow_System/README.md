# A2 University Library Borrow System

ระบบยืม-คืนหนังสือมหาวิทยาลัยด้วย Python

## Features
- Class and Object
- 2D Array
- Function Design
- Borrow book
- Return book
- Search book
- Check overdue
- File Read/Write (CSV)
- Try-Except
- Error handling

## Requirements
- Python 3.9 or newer
- No external libraries required

## Run

เปิด Terminal ในโฟลเดอร์โปรเจกต์ แล้วใช้:

```bash
python main.py
```

หรือบางเครื่อง:

```bash
python3 main.py
```

## Menu

1. Show books
2. Search book
3. Borrow book
4. Return book
5. Check overdue
6. Show borrow records
7. Save data
0. Exit

## GitHub

ตัวอย่างคำสั่ง:

```bash
git init
git add .
git commit -m "Create A2 university library borrow system"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## Demo ที่ควรแสดง
1. แสดงรายการหนังสือ
2. ค้นหาหนังสือ
3. ยืมหนังสือด้วยข้อมูลถูกต้อง
4. ลองใช้ Student ID ที่ไม่มี
5. ลองใช้ Book ID ที่ไม่มี
6. แสดงรายการยืม
7. คืนหนังสือ
8. ตรวจสอบ overdue
9. แสดงไฟล์ CSV
10. อธิบาย Error Log และวิธีแก้

## หมายเหตุ
ไฟล์ `data/borrow_records.csv` จะถูกสร้าง/อัปเดตอัตโนมัติเมื่อโปรแกรมบันทึกข้อมูล
