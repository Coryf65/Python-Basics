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
    print('there are {0} tickets remaining.'.format(GetTicketsRemaining()))
    current_user = input('Please enter your name, ')
    print('Welcome , {}'.format(current_user))

    num_tickets = input('How many tickets would you like to purchase? ')
    
    # TODO error here, we get a ValueError
    try:
        num_tickets = int(num_tickets)
        # Raise a ValueError if the request is for more than available
        if num_tickets > tickets_remaining:
            raise ValueError('There are only {0} tickets remaining'.format(tickets_remaining))
    except ValueError as err:
        # inclue the error text in the output
        print('oh no, we ran into an issue. {0}. Please try again'.format(err))
    else:
        print('That would be ${0}'.format(CalculateTicketPrice(num_tickets)))

        # if they want to proceed Y/N
        should_proceed = input('Would you like to purchase?  Y/N,   ')
        if should_proceed.lower() == 'y':
            # TODO: Gather Creditcard info and process
            print('SOLD!')
            tickets_remaining -= num_tickets
        else:
            # thank them by name
            print('Thank you anyways, {0}'.format(current_user))
# notify that we are sold out
print('Sorry we are all sold out! ')
