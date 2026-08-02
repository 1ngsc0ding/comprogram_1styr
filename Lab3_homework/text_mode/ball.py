# รับค่าจำนวนลูก Football, Basketball, Volleyball แล้วแสดงว่ามีจำนวนลูกอะไรมากที่สุด
# ให้ใช้ตัวแปร integer 3 ตัวเก็บค่า
# และทำการเปรียบเทียบพื้นฐานเท่านั้น (เพื่อฝึกการใช้คำสั่งเงื่อนไข)

football = int(input("Enter number of Football: "))
basketball = int(input("Enter number of Basketball: "))
volleyball = int(input("Enter number of Volleyball: "))

if football > basketball and football > volleyball:
    print("Football has the most balls")

elif basketball > football and basketball > volleyball:
    print("Basketball has the most balls")

elif volleyball > football and volleyball > basketball:
    print("Volleyball has the most balls")

else:
    print("There is a tie")