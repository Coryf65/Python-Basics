import math

# Global Vars
TICKET_PRICE = 10
tickets_remaining = 100

## Output how many tickets are remaining
def GetTicketsRemaining():
    return tickets_remaining

def CalculateTicketPrice(tickets):
    return math.ceil(tickets * TICKET_PRICE)

while tickets_remaining >= 1:
    print('You have {0} tickets left.'.format(GetTicketsRemaining()))
    current_user = input('Please enter your name, ')
    print('Welcome , {}'.format(current_user))

    tickets_to_buy = input('How many tickets would you like to purchase? ')
    tickets_to_buy = int(tickets_to_buy)

    print('That would be ${0}'.format(CalculateTicketPrice(tickets_to_buy)))

    # if they want to proceed Y/N
    should_proceed = input('Would you like to purchase?  Y/N,   ')
    if should_proceed.lower() == 'y':
        # TODO: Gather Creditcard info and process
        print('SOLD!')
        tickets_remaining -= tickets_to_buy
    else:
        # thank them by name
        print('Thank you anyways, {0}'.format(current_user))

# notify that we are sold out
print('Sorry we are all sold out! ')
