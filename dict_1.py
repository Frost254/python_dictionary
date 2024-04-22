import json

with open('data.json') as json_file:
    data = json.load(json_file)

# Print the type of data variable
    print("Type:", type(data))

#create a function that defines the definition of a word

word = input("Enter the word to define: ")
word = word.lower()
def define(user_input):
    user_input = word
    if user_input in data:
        print(data[user_input])
    else:
        print("Word not found")

define(word)
