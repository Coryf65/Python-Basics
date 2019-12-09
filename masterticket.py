import math

# Global Vars
TICKET_PRICE = 10
tickets_remaining = 100


def get_tickets_remaining():
    return tickets_remaining

# Calculate the price function
def calculate_ticket_price(tickets):
    return math.ceil(tickets * TICKET_PRICE)

while tickets_remaining >= 1:
    print('there are {0} tickets remaining.'.format(get_tickets_remaining()))
    current_user = input('Please enter your name, ')
    print('Welcome , {}'.format(current_user))

    num_tickets = input('How many tickets would you like to purchase? ')
    
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError('There are only {0} tickets remaining'.format(tickets_remaining))
    except ValueError as err:
        print('oh no, we ran into an issue. {0}. Please try again'.format(err))
    else:
        print('That would be ${0}'.format(calculate_ticket_price(num_tickets)))
        should_proceed = input('Would you like to purchase?  Y/N,   ')
        if should_proceed.lower() == 'y':
            # TODO: Gather CC info and process payment
            print('SOLD!')
            tickets_remaining -= num_tickets
        else:
            print('Thank you anyways, {0}'.format(current_user))

# notify that we are sold out
print('Sorry we are all sold out! ')
