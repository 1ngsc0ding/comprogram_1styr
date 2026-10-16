# write functions to
# a. search for a character in a string (return index),
# starting from the left-hand side (index=0 )

# b. search for a character in a string (return index),
# starting from the right-hand side (index=length-1)

# e. boolean function to check whether a given string is a palindrome
# (using while loop) start with simple strings

# "Deed"
# "An na"
# "BKKrotorKKB"
# "25/8/52"

# See https://en.wikipedia.org/wiki/Palindrome

def main():
    word = input("Enter a string: ")

    # Check the index of 'a' from left
    def character_check_left(char, word):
        i = 0 # Check from left
        while i < len(word):
            if word[i] == char: 
                return i
            i += 1
        return -1

    check_left = character_check_left("a", word)

    # Check the index of character from right
    def character_check_right(char, word):
        i = len(word) - 1 # Check from right
        while i >= 0:
            if word[i] == char:
                return i
            i -= 1
        return -1

    check_right = character_check_right("a", word)

    # Palindrom check, palindrome = readable the same backward as forward
    def check_palindrome(word):
        # Check if the first and last are the same
        while (word[0] == word[-1]):
            word = word[1:-1]
            if len(word) <= 1: 
                return True
        return False

    palindrome_result = check_palindrome(word)

    if palindrome_result is True:
        print(f"{word} is a palindrome.")
    else:
        print(f"{word} is not a palindrome.")

    print(f"First 'a' was found at index {check_left} from the left.")
    print(f"First 'a' was found at index {check_right} from the right.")


main()
