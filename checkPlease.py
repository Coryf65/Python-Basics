import math

# now doing exception handling

# spit the cost into x amount of peeps
def split_check(total, num_of_people):
    return math.ceil(total / num_of_people)


# store function into amount due
#amount_due = split_check(84.97, 4)

# now taking user input

try:
    total_due = float(input("What is the total?  "))
    number_of_people = int(input("How many people?  "))
except ValueError:
    print("Oh nooo That's not a Valid Value, try again")
else:
    amount_due = split_check(total_due, number_of_people)
    print("Each person owes ${}".format(amount_due))

