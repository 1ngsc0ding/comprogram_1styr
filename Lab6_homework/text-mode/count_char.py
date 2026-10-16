# ให้นักศึกษาเขียนโปรแกรม ที่มีฟังก์ชันต่อไปนี้
#   ฟังก์ชันชื่อ countChar เพื่อนับจํานวนตัวอักษรใน String
#   เช่น print( countChar( "a" , "Thailand" ) )
#   จะแสดงค่า 2 เพราะมีa สองตัวในคําว่า Thailand

vocab = input("Enter a string: ")
char = input("Enter a character to count: ")

def countChar(char, vocab):
    count = 0
    i = 0
    while i < len(vocab):
        if vocab[i] == char:
            count += 1
        i += 1
    return count

print(f"The character '{char}' appears {countChar(char, vocab)} times in the string '{vocab}'.")