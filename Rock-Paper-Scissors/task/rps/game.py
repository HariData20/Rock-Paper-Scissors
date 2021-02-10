# Write your code here
import random
import sys

name = input('Enter your name:')
print('Hello, {}'.format(name))
score = 0
selection = input()
if selection == '':
    options = ['rock', 'paper', 'scissors']
else:
    options = selection.split(',')
print("Okay, let's start")
# rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire
winning_cases = {
    'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}
with open('rating.txt', 'r') as f:
    for line in f:
        if name in line:
            score = int(line.split(' ')[1])
            break
while True:
    choice = input()
    if choice in options:
        system_choice = random.choice(options)
        if choice == system_choice:
            print("There is a draw ({})".format(system_choice))
            score += 50
        elif system_choice in winning_cases.get(choice):
            print('Well done. The computer chose {} and failed'.format(system_choice))
            score += 100
        else:
            print('Sorry, but the computer chose {}'.format(system_choice))
    elif choice == '!rating':
        print('Your rating:', score)
    elif choice == '!exit':
        print('Bye!')
        sys.exit()
    else:
        print("Invalid input")

"""

if choice == 'scissors' and system_choice == '':
    print('Sorry, but the computer chose rock')
elif choice == 'paper':
    print('Sorry, but the computer chose scissors')
else:
    print('Sorry, but the computer chose paper')
"""
