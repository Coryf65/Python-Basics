# learning about python Operators!

# alphabetically higher, returns True
print("sunshine" > "rain")


# fun quiz

first_name = input("What is your first name?  ")

print("Hello", first_name)

# if else branch
if first_name == "Cory":
    # if true
    print("Hey me..")
    print(first_name, "is learning Python !")
elif first_name == "Maximiliane":
    print(first_name, "is learning with others in the community! me too!")
else:
    #casting to an int
    age = int(input("How old are you?  "))
    if age <= 6:
        print("Wow you're {}! If you're confident with reading already...".format(age))
    print("You should totally learn Python!")

print("Have a great Day {}!".format(first_name))