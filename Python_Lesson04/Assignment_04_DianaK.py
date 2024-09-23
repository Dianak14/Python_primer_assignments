# Create user input variable 
user_word = input("Enter a word: ")

# Create a list from the user input
letters_in_word = list(user_word)

print (letters_in_word)

# reverse the letters in the list
letters_in_word.reverse()

# Create a new string from the letters that have been reversed 
reversed_user_word = "".join(letters_in_word)

# Use boolean to check if user_word is the same as reversed_user_word to confirm it is a palindrome 
if reversed_user_word == user_word:
    print (True)
else:
    print (False)