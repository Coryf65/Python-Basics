import math

# now doing exception handling

# spit the cost into x amount of peeps
def split_check(total, num_of_people):
    if num_of_people <= 1:
        raise ValueError("More than one person is required to split the check")
    return math.ceil(total / num_of_people)


# store function into amount due
#amount_due = split_check(84.97, 4)

# now taking user input

try:
    total_due = float(input("What is the total?  "))
    number_of_people = int(input("How many people?  "))
    amount_due = split_check(total_due, number_of_people)
except ValueError as err:
    print("Oh nooo That's not a Valid Value, try again")
    print("({})".format(err))
else:    
    print("Each person owes ${}".format(amount_due))

