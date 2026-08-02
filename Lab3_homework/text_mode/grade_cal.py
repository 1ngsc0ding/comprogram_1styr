# Calculate grade from score (A for score 80-100, B for 70-79, C for 60-69 and D for
# 50-59, F for 0-49)

score = float(input("Insert your score: "))

def grade_calculator(score):
    if 80 <= score <= 100:
        return "A"
    elif 70 <= score < 80:
        return "B"
    elif 60 <= score < 70:
        return "C"
    elif 50 <= score < 60:
        return "D"
    elif 0 <= score < 50:
        return "F"
    else:
        return "Invalid score"
    
print(f'Your grade is {grade_calculator(score)}')
