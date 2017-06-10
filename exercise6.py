

word = input("Enter a word: ")
reverse = word[::-1]

if word != reverse:
    print(word + " and " + reverse + " are not palindromes")
else:
    print(word + " and " + reverse + " are palindromes!!!")
