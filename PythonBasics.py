#Python uses Snake Case for naming conventions
first_name = "Ada" 
last_name = "Lovelace"

print("Hello," + first_name + " ")
print(first_name + " " + last_name + " is an awesome person!")

# print() automatically adds spaces
print("These", "will be joined", "together by spaces!")

# Python will save vars like JS kinda
is_int = 12

print(is_int)


# getting user input and saving as a var
current_mood = input("How are you today ?  ")

# displaying the mood !
print("I am glad that you are ,", current_mood)

# PEMDAS...
print("PEMDAS: ", 0.1 + 0.1 + 0.1 - 0.3)

# we get 0.0000005
# now we can round this
print("rounding: ",round(0.1 + 0.1 + 0.1 - 0.3))


# this Method helps give info about the passed in function or Argument!
help(str)