# Create the vowel counter module 

# Create the function to take in a 'name' input
def vowel_counting(name):
    # Note the vowels to be identified, covering both uppercase and lowercase
    vowels = "AIEOUaeiou"

    # count the number of vowels in the name passed as the input
    vowel_count = sum(1 for char in name if char in vowels)

    # Print the result 
    print (f"My name is {name}. ")
    print(f"I have {vowel_count} vowels in my name. ")