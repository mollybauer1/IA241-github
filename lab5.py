"""
lab 5
"""
#3.1
alien_color = 'green'
if alien_color == 'green':
    print('you got 5 points')

#3.2
alien_color = 'yellow'
if alien_color == 'green':
    print('you got 5 points')
else:
    print('you got 10 points')
    
#3.3
favorite_fruits = ['apple', 'orange', 'grape']
if ('grape' in favorite_fruits):
    print('You really like grapes!')
if ('watermelon' in favorite_fruits):
    print('You really like watermelon!')
if ('orange' in favorite_fruits):
    print('You really like oranges!')

#3.4
age = 19
if age<10:
    print('Kid')
elif (age<20):
    print('Teenager')
elif (age>= 65):
    print("Elder")
else:
    print("Adult")