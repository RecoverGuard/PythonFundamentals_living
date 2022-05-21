#RecoverGuard_2022
#this is a dice roll simulator

import random

min = 1
max = 6

roll_again = 'Y'
good_bye = 'N'


while roll_again == 'Y':
    print('Rolling the dice...')
    print('You rolled:')
    print(random.randint(min, max))
    print(random.randint(min, max))

    roll_again = (input('Roll the dice again? Y/N '))

while good_bye == 'N':
    print(input('Good-Bye'))



