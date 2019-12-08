import math

TICKET_PRICE = 10

tickets_remaining = 100

# STEP 1, as a User I should be shown the number of tickets left remaining

## Output how many tickets are remaining
def GetTicketsRemaining():
    return tickets_remaining


def CalculateTicketPrice(tickets):
    return math.ceil(tickets * TICKET_PRICE)

print('You have {0} tickets left.'.format(GetTicketsRemaining()))

# STEP 2, have a personalized expeirence for our brand

#  gather the users name and assign to a var
current_user = input('Please enter your name, ')

#prompt the user by name and ask how many tickets they would like
print('Welcome , {}'.format(current_user))

tickets_to_buy = input('How many tickets would you like to purchase? ')
tickets_to_buy = int(tickets_to_buy)

# calculate the cost of how many tickets * the price 
# output to price to the screen
print('That would be ${0}'.format(CalculateTicketPrice(tickets_to_buy)))

# if they want to proceed Y/N
should_proceed = input('Would you like to purchase?  Y/N,   ')
# If they do
if should_proceed.lower() == 'y':
    # print out 'SOLD!' to confirm the purchase
    # TODO: Gather Creditcard info and process
    print('SOLD!')
    # and then decrement the tickets remaing by the num of tickets purchased
    tickets_remaining -= tickets_to_buy

# otherwise
else:
    # thank them by name
    print('Thank you anyways, {0}'.format(current_user))
