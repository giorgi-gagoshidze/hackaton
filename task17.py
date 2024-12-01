from random import randint
num1 = randint(1, 10)
num2 = int(input('guess number from 1-10: '))
while num2 != num1:
    num2 = int(input('try again: '))
print('congrats you win')