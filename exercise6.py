"""
# This is option 1 without loop
word = input("Enter a word: ").lower()
reverse = word[::-1]

if word != reverse:
    print(word + " is not a palindrome")
else:
    print(word + " is a palindrome!!!")
"""
# This is option 2 with a loop
def reverse_word(word):
    reverse_word = ""
    for x in range(len(word)):
        reverse_word += word[len(word) - 1 - x]
    return reverse_word

word = input("Enter a word: ").lower()
reverse_word = reverse_word(word)

if word != reverse_word:
    print(word + " is not a palindrome")
else:
    print(word + " is a palindrome!!!")
