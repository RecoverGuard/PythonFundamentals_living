#sentence guessing game

secret_word = 'crazy'


print('Welcome to Secret Word! You have THREE tries to complete my sentence. Good luck!')
user_word = input('The entire year of 2020 has been: ')
print(user_word)

if user_word == secret_word:
    print('Congratulations, you finished the sentence!')
else:
    print("Sorry, you weren't even close, pal.")
    print('Clue 1: Five letter word starting with C.')
    user_word = input('Guess again: ')
    if user_word == secret_word:
        print('Congratulations, you finished the sentence!')
    else:
        print('OOF, wrong! but you are getting warmer.')
        print('Clue 2: It is a synonym for insane.')
        user_word = input("This is your last guess. don't screw it up, Chief: ")
        if user_word == secret_word:
            print('Congratulations, you finished the sentence!')
        else:
            print("Wow...Don't quit your day job. The secret word was: {}".format(secret_word))