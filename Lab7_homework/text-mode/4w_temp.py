# กําหนดให้ใช้อะเรย์2 มิติ เก็บข้อมูลอุณหภูมิเป็นเวลา 4 สัปดาห์สัปดาห์ละ 7 วัน
# (โดยแต่ละแถวแทน 1 สัปดาห์ และแต่ละคอลัมน์แทน 1 วัน)
# และให้นักศึกษาเขียนฟังก์ชันเพื่อหาค่าต่อไปนี้
# - ค่าอุณหภูมิเฉลี่ยของสัปดาห์ที่ต้องการ week_average()
# - ค่าอุณหภูมิสูงสุดของสัปดาห์ที่ต้องการ week_max()
# - ค่าอุณหภูมิต่ําสุดของสัปดาห์ที่ต้องการ week_min()
# ให้นศ.กําหนดพารามิเตอร์ที่เหมาะสม เพื่อระบุสัปดาห์ที่ต้องการได้
# เช่น w = 0 สัปดาห์แรก, w = 1 สัปดาห์ที่สอง

# จากนั้นให้ใช้week_max() เพื่อหา
# - ค่าอุณหภูมิสูงสุดจากข้อมูลทั้งหมด overall_max()
# และ week_min() เพื่อหา
# - ค่าอุณหภูมิต่ําสุดจากข้อมูลทั้งหมด overall_min()

weekly_temp = [[35, 36, 36, 34, 34, 34, 33],[33, 32, 31, 32, 31, 31,31], [31, 31, 30, 31, 31, 32, 31], [32, 31, 31, 32, 31, 32, 31]]

w = int(input("Enter week (0-3): "))

def week_average(weekly_temp, w):
    total = 0
    d = 0
    while d < 7:
        total += weekly_temp[w][d]
        d += 1
    return total / 7
print("Average:", week_average(weekly_temp, w))


def week_max(weekly_temp, w):
    maximum = weekly_temp[w][0]
    d = 1
    while d < 7:
        if weekly_temp[w][d] > maximum:
            maximum = weekly_temp[w][d]
        d += 1
    return maximum
print("Max:", week_max(weekly_temp, w))


def week_min(weekly_temp, w):
    minimum = weekly_temp[w][0]
    d = 1
    while d < 7:
        if weekly_temp[w][d] < minimum:
            minimum = weekly_temp[w][d]
        d += 1
    return minimum
print("Min:", week_min(weekly_temp, w))

def overall_max(weekly_temp):
    maximum = week_max(weekly_temp, 0)
    w = 1
    while w < 4:
        if week_max(weekly_temp, w) > maximum:
            maximum = week_max(weekly_temp, w)
        w += 1
    return maximum
print("Overall max:", overall_max(weekly_temp))

def overall_min(weekly_temp):
    minimum = week_min(weekly_temp, 0)
    w = 1
    while w < 4:
        if week_min(weekly_temp, w) < minimum:
            minimum = week_min(weekly_temp, w)
        w += 1
    return minimum
print("Overall min:", overall_min(weekly_temp))







