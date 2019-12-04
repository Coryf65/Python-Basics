import math

# spit the cost into x amount of peeps
def split_check(total, num_of_people):
    cost_per_person = math.ceil(total / num_of_people)
    return cost_per_person

# store function into amount due
#amount_due = split_check(84.97, 4)

# now taking user input
total_due = float(input("What is the total?  "))
number_of_people = int(input("How many people?  "))

amount_due = split_check(total_due, number_of_people)

# display
print("Each person owes ${}".format(amount_due))