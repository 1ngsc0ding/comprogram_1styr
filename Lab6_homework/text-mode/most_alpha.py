text = input("Enter string: ")

def countChar(char, text):
    count = 0
    index = 0

    while index < len(text):
        if text[index] == char:
            count += 1
        index += 1
    return count

def mostFrequentChar(text):
    maxChar = ""
    maxCount = 0
    index = 0

    while index < len(text):
        char = text[index]
        count = countChar(char, text)
        if count > maxCount:
            maxCount = count
            maxChar = char
        index += 1
    return maxChar, maxCount

char, count = mostFrequentChar(text)

print("Character:", char)
print("Count:", count)