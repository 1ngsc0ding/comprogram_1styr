# สมมุติเกมทายตัวเลข ให้โปรแกรมกําหนดตัวเลขจํานวนเต็ม (หรือสุ่มตัวเลข)
# ตั้งแต่ 1 ถึง 100 ให้เป็นค่าของตัวแปร x

# เริ่มเล่นโดยให้ผู้ใช้เดาและใส่ค่าตัวเลขจํานวนเต็ม
# - ถ้าผู้ใช้เดาถูกต้อง จะจบเกม
# - ถ้าเดาไม่ถูก จะบอกว่าค่าที่ใส่มานี้มีค่ามากกว่าหรือน้อยกว่า ค่าของ x
# แล้วจะให้ผู้ใช้เดาและใส่ค่าตัวเลขอีกครั้ง จนกว่าจะเดาถูก และจบโปรแกรม
# - ผู้ใช้สามารถเลิกเล่นก่อนได้ โดยใส่เลข 0 เพื่อให้โปรแกรมเฉลยค่าของ x และจบโปรแกรม

import random

num = random.randint(1, 100)

while True:
    guess = int(input("Guess the number (1-100) or enter 0 to quit: "))
    
    if guess == 0:
        print(f"The number was: {num}. Thanks for playing!")
        break
    elif guess < num:
        print("Too low! Try again.")
    elif guess > num:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {num} correctly!")
        break

