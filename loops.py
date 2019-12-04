import sys

# password checker loop!
MASTER_PASSWORD = 'open me'
password = input("Please enter a super secret password:  ")
attempt_count = 1

while password != MASTER_PASSWORD:

    if attempt_count > 3:
        exit("Too many Invalid Password attempts")
    password = input("Invalid Password please try again:  ")
    attempt_count += 1   

print("Welcome to secret town")