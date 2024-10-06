print("Welcome to the palindrome checker")

user_input = input("Enter a word or phrase to check: ")

# normalise the input

normalised_input = ''
for char in user_input:
    if char.isalpha():
        normalised_input += char.lower()

# Check if the newly normalised string is a palindrome
if normalised_input == normalised_input[::-1]:
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')

