# สมมุติชาวสวนทุเรียนแห่งหนึ่ง ต้องการโปรแกรมสําหรับ นับจํานวนของลูกทุเรียน และ น้ําหนักเฉลี่ยของทุเรียน
# ทั้งหมด โดยต้องการจะรับค่าน้ําหนักของทุเรียน ทีละ 1 ลูก
# ถ้าหมดแล้วจะใส่ค่าน้ําหนักของทุเรียน เป็นศูนย์(zero) โปรแกรมจึงจะแสดงค่าจํานวนของลูกทุเรียน และ น้ําหนัก
# เฉลี่ยของทุเรียนทั้งหมด ตัวอยาง เชน

# Please input Durian weight: 3
# Please input Durian weight: 5
# Please input Durian weight: 4
# Please input Durian weight: 0

# Total of 3 Durians
# Average weight is 4

def calculate_durian_weight():
    count = 0
    total = 0

    durian = int(input("Please input Durian weight: "))

    while durian != 0:
        count = count + 1
        total = total + durian

        durian = int(input("Please input Durian weight: "))

    if count > 0:
        average = total / count
    else:
        average = 0

    print("Total of", count, "Durians")
    print("Average weight is", average)


calculate_durian_weight()
