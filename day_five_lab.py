#lab for day 5 of python basics

#variables

#primary number types in python: integers and floating points


x = 5 #integer

pi = 3.14
radius = 2.47

print(float(pi * radius **2))

name = 'James'
surname = 'Vinciguerra'

# this is a string

print(name.lower()  + ' ' + surname.upper())

question = input('is basic training difficult? Y/N: ')

if question == 'Y':
    print('You probably were too soft anyway!')
else:
    print('You are a hard charging warrior!')


budget = float(input('What is your monthly grocery budget in dollars between $1 and $1000? $'))


if budget > 1001:
    print('ERROR, this is not a valid entry')
elif budget > 550:
    print('You will eat well this month!')
elif budget >= 550:
    print('This is the average American food budget')
elif budget <= 0:
    print('ERROR, this is not a valid entry')
else:
    print('This is less than the average American food budget')



#loops and data structure

x = 0
while x <= 100:
    print(x)
    x = x + 2

#commenting out the code to stop multiple counters from running
#for i in range(2, 100):
    #if i%2 == 0:
        #print(i)


nums = []
import random

for z in range(100):
    nums.append(random.randint(1,100))

print(nums)







