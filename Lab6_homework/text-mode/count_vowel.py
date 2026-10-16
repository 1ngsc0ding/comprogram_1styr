# ฟังก์ชันชื่อ countVowels เพื่อนับจํานวนตัวสระ (aeiou) ใน String
# เช่น print( countVowels("Bangkok") )
# จะแสดงค่า 2 เพราะมีสระสองตัวในคําว่า Bangkok
# และฟังก์ชันนี้ต้องมีการเรียกใช้ countChar() สําหรับหาจํานวนตัวอักษร

vocab = input("Enter a string: ")

def check_vowel(char):
    vowels = "aeiou"
    return char in vowels

def countVowels(vocab):
    count = 0
    for char in vocab:
        if check_vowel(char):
            count += 1
    return count

print(f"The number of vowels in '{vocab}' is {countVowels(vocab)}.")