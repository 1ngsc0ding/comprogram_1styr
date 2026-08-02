# คํานวณพื้นที่ของที่ดินรูปสี่เหลี่ยม จากความกว้างและความยาว (หน่วยเป็นเมตร)
# แสดงพื้นที่ในหน่วยตารางเมตร และระบุว่ามีพื้นที่เพียงพอสําหรับแข่งขันกีฬาอะไรได้บ้าง เช่น
# Football, Basketball, Volleyball (หรือกีฬาอื่นๆที่นศ.สนใจ)
# และเมื่ออ่านบทที่ 6 จบแล้ว ควรทดลองสร้าง boolean function

def calculate_area(width, length):
    return width * length


def can_play_sport(area, sport_area):
    return area >= sport_area


width = float(input("Enter land width (meter): "))
length = float(input("Enter land length (meter): "))

area = calculate_area(width, length)

print(f"Land area = {area} square meters")

# พื้นที่ขั้นต่ำโดยประมาณ
football_area = 4050      # 45 x 90 m
basketball_area = 420     # 15 x 28 m
volleyball_area = 162     # 9 x 18 m

print("\nSuitable sports:")

if can_play_sport(area, football_area):
    print("- Football")

if can_play_sport(area, basketball_area):
    print("- Basketball")

if can_play_sport(area, volleyball_area):
    print("- Volleyball")

if not (can_play_sport(area, football_area) or
        can_play_sport(area, basketball_area) or
        can_play_sport(area, volleyball_area)):
    print("- No standard sport field available")
    