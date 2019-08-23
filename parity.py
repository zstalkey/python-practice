## TASK 1

# given a 5x5 grid, add the last column and row, then flip the card at the
# coordinate specified by the user
five_by_five_grid = [
    ['X','0','X','X','X'],
    ['X','X','0','0','0'],
    ['X','0','X','0','X'],
    ['0','X','X','X','X'],
    ['X','0','0','X','X'],
]

# first step is to add colum 6 and row 6
# If 'X' is even add '0", if 'X' is odd add 'X'

x = five_by_five_grid.count('X')

print(x)

# for row in five_by_five_grid:
#     if (x%2) == 0:
#         five_by_five_grid.append('0')
#     else:
#       five_by_five_grid.append('X')  

# # output the grid to the user
# for five_by_five_grid in five_by_five_grid:
#     print(five_by_five_grid)        

# ask the user for the coordinate of the card to flip
# e.g. input could be: (0,2)

# x = input('Input a row coordinate')
# y = input('Input a column coordinate')

# for five_by_five_grid in five_by_five_grid:
#     if coorinate 

# output the grid with the flipped card

## TASK 2

# given a six by six grid, work out what card was flipped

# your program should output the coordinate of the flipped card
# in this case it would be: (x,y)