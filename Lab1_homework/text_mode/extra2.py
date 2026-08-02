# KMUTNB Computer Engineering TCAS69 Admission Score Calculator

# Display the program title
print("=" * 50)
print("KMUTNB COMPUTER ENGINEERING")
print("TCAS69 ADMISSION CALCULATOR")
print("=" * 50)

# Acquire the user's academic information
gpax = float(input("GPAX: "))
tpat3 = float(input("TPAT3: "))
math1 = float(input("A-Level Mathematics 1: "))
physics = float(input("A-Level Physics: "))
chemistry = float(input("A-Level Chemistry: "))
english = float(input("A-Level English: "))

# Calculate the weighted score for each subject
tpat3_score = tpat3 * 0.25
math_score = math1 * 0.25
physics_score = physics * 0.20
chemistry_score = chemistry * 0.10
english_score = english * 0.20

# Calculate the final admission score
final_score = tpat3_score + math_score + physics_score + chemistry_score + english_score

# Display the admission score report
print("===== ADMISSION REPORT =====")
print("GPAX:", gpax)

# Display each weighted subject score
print("TPAT3       :", round(tpat3_score, 2))
print("Mathematics :", round(math_score, 2))
print("Physics     :", round(physics_score, 2))
print("Chemistry   :", round(chemistry_score, 2))
print("English     :", round(english_score, 2))

print("-" * 28)

# Display the final weighted score
print("Final Score :", round(final_score, 2))

# Display the minimum GPAX requirement
print("Required GPAX >= 2.75")