#Exercise 1
# try: 
#     num1 = int(input('Please enter a number: '))
#     print(num1 * 10)
# except: 
#     print('Woops! That\'s not a number, please try again!')
#     num1 = int(input('Please enter a number: '))
#     print(num1 * 10)

#Exercise 2
string = input("Type in a word or sentence: ")
if string.isdigit():
    print('Woops! That\'s an integer, try again!')
    string = input("Type in a word or sentence: ")
if '.' in string:
    val = float()
    print ('Woops That\'s a float, try again!')
    string = input("Type in a word or sentence: ")
else: print(string)