# Common string methods from the slides
examples = ["Hello", "A", "3"]
for value in examples:
    print(repr(value), "upper:", value.upper(), "lower:", value.lower())
    print("isalpha:", value.isalpha(), "isdigit:", value.isdigit(), "isalnum:", value.isalnum())

text = "Hello"
result = ""
index = 0
while index < len(text):
    result += str(index)
    index += 1
print("Index string:", result)
