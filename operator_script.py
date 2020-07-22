# We're going to read in a number from the user input
#we want to see if the number is greater than 50

read_number = int(input('Enter your number here: '))

print('Your number is {}'.format(read_number))

#write the comparison operator to check if read_number is greater than 50

if read_number > 50:
    print('Your number is greater than 50')

if read_number <= 50:
    print('Your number is not greater than 50')

