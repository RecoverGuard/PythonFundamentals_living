<<<<<<< HEAD
#this is a secret number game

import random
num = (random.randint(1, 100))
user_num = 0

print('Welcome to the Secret Number Game! Test your luck!')

while num != user_num:
    user_num = int(input('please select a number from 1-100: '))

    if user_num > num:
        print('Your guess is too high, please try again...')

    if user_num < num:
        print('Your guess is too low, please try again...')

    if user_num == num:
        print('The secret number was {}!'.format(num))
        print('You win the game!')
=======
#this is a secret number game

import random
num = (random.randint(1, 100))
user_num = 0

print('Welcome to the Secret Number Game! Test your luck!')

while num != user_num:
    user_num = int(input('please select a number from 1-100: '))

    if user_num > num:
        print('Your guess is too high, please try again...')

    if user_num < num:
        print('Your guess is too low, please try again...')

    if user_num == num:
        print('The secret number was {}!'.format(num))
        print('You win the game!')
>>>>>>> b2b3c7740bf8de2a9de90df927f7a5ccbf8e6c87
