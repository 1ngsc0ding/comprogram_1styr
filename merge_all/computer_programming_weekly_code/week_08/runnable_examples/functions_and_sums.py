# Week 08: functions, parameters, return values and ranges
def sum_1_to_n(n):
    total = 0
    count = 1
    while count <= n:
        total += count
        count += 1
    return total

def sum_m_to_n(m, n):
    total = 0
    count = m
    while count <= n:
        total += count
        count += 1
    return total

def main():
    for number in (5, 10):
        print(f"Sum from 1 to {number} = {sum_1_to_n(number)}")
    print("Sum from 3 to 7 =", sum_m_to_n(3, 7))

if __name__ == "__main__":
    main()
