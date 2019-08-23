#conditionals
#variables should never start with capitals or numbers
#If they are multiple words long, no spaces or underscores. zoeIsAwesome or zoe_is_awesome

# raining = True
# raining_hard = True
# sunny = False

# if raining: 
#     print('Take an umbrella')
#     if raining_hard: 
#         print('and a jacket')
# elif sunny: 
#     print('Wear a hat')
# else:
#     print('Leave the umbrella at home')

# level = 10

# if level >= 10: 
#     print('woohoo! over 10!')
# else: 
#     print('under 10')

# animal = 'cat'
# if animal == 'cat':
#     print('meow')
# else: 
#     print('woof')




#---------------IN CLASS EXERCISES-------------------
# #Exercise 1
# x = int(input('Pick a number'))
# y = int(input('Pick another number'))
# if x < y:
#     print('Largest number is', y)
# elif y == x: 
#     print('The numbers you entered are the same.')
# else: 
#     print('largest number is', x)

# #Exercise 2
# xy = int(input('Choose a number'))
# if xy > 5: 
#     print('True')
# elif xy == 5:
#     print('The integer is exactly 5.')
# else: 
#     print('False')

# #Exercise 3
# question = input('Write hayley is awesome!')
# if question == 'hayley is awesome!':
#     print('True')
# else: 
#     print('False')

# #Exercise 4
def birthday(name, age):
    if age > 30:
        print(name, 'is at level', age)
    elif age == 30:
        print(name, 'is', age, '!!')
    else:
        print(name, 'is', age, 'years old')

birthday (input('what is your name'), int(input('what is your age')))