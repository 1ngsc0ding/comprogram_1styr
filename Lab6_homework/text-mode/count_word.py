# ฟังก์ชันชื่อ countWords เพื่อนับจํานวนคํา ใน String
# เช่น print( countWords("Human and AI can make mistakes") )
# จะแสดงค่า 6 เพราะมีสระสองตัวในคําว่า Bangkok

def countWords(text):
    count = 0
    index = 0
    in_word = False

    while index < len(text):
        if text[index] != " " and in_word == False:
            count += 1
            in_word = True
        elif text[index] == " ":
            in_word = False
        index += 1
    return count

print(countWords("Everyone can make mistakes"))