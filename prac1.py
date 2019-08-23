# # #Exercise 1
# x = int(input('Pick a number'))
# y = int(input('Pick another number'))
# if x < y:
#     print('Largest number is', y)
# elif y == x: 
#     print('The numbers you entered are the same.')
# else: 
#     print('largest number is', x)

# # #Exercise 2
# xy = int(input('Choose a number'))
# if xy > 5: 
#     print('True')
# elif xy == 5:
#     print('The integer is exactly 5.')
# else: 
#     print('False')

# # #Exercise 3
# question = input('Write hayley is awesome!')
# if question == 'hayley is awesome!':
#     print('True')
# else: 
#     print('False')

# #Exercise 4
def birthday(name, age):
    message1_template = '{name} is at level {age}.' #Can format outside#
    message2 = '{name} is {age} !!' .format(name=name, age=age)
    message3 = '{name} is {age} years old' .format(name=name, age=age)
    if age > 30:
        print(message1_template.format(name, age)) #formated outside#
    elif age == 30:
        print(message2)
    else:
        print(message3)

birthday (input('what is your name'), int(input('what is your age')))