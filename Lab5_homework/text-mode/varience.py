# ให้นักศึกษาเขียนฟังก์ชันที่รับพารามิเตอร์เป็นอะเรย์ของจํานวนเต็ม (integer)
# และ return ค่าความแปรปรวน (Variance)
# โดยนักศึกษาฝึกเขียนโปรแกรมเพื่อคํานวณค่าเอง (ไม่เรียกใช้Built-in Function)

numbers = [10, 20, 30, 40, 50]

def find_variance(arr):
    total = 0
    i = 0

    while i < len(arr):
        total = total + arr[i]
        i = i + 1

    average = total / len(arr)

    total_square = 0
    i = 0

    while i < len(arr):
        difference = arr[i] - average
        total_square = total_square + difference * difference
        i = i + 1

    variance = total_square / len(arr)

    return variance

result = find_variance(numbers)

print("Variance =", result)
