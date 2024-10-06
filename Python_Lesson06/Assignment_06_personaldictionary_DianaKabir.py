# Create variable with name and an associated dictionary
Diana = {
    "name": "Diana",
    "age" : 40,
    "gender": "Female",
    "city" : "Sydney",
    "occupation" : "Student",
    "hobby" : "reading"
}

# Use loop to print all the key value pairs in the dictionary 
for key, value in Diana.items():
    print(f"My {key} is {value}.")

# Add an additional key value pair 
Diana["favourite food"] = "pasta"

print(Diana)

# Delete a key value pair 
Diana.pop("age")

print(Diana)

# Amend a key value pair
Diana_new ={"hobby": "swimming"}
Diana.update(Diana_new)
print(Diana)

#clear the dictionary 
Diana.clear()
print(Diana)