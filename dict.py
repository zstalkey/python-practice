#people = {}
#print (people)

# people = {
#     'hayley': 'lead instructor',
#     'nanwen': 'coder'
# }
# print (people)

# people['chloe'] = 'wears glasses'
# people['hayley'] = 'is wearing red'

# print (people)


#use a for loop to print out each key and value in a dict. 
#chloe: wears glasses


#TASK 1
# dogs = {
#     'helen': 'is a white dog',
#     'susan': 'is a white dog',
#     'lily': 'is a brown dog', 
#     'soda': 'is a blue dog'
# }

# for dogs in colour: 
#     print ('{key} : {value}'.format(
#         key=dogs,
#         value=dogs[colour]
#         )
#     )

#TASK2

    #given the list of names, create a dictonary where the key is the index and the value is the name.
    #ie. after adding the first name, the dictionary would look like this
    #(0:'chloe')

# names = ['chloe', 'cass', 'sarah', 'ellie', 'maddy']

# for index, name in enumerate(names):
#     print(index,name)

# peoplenames = {}

# peoplenames[0] = 'chloe'
# peoplenames[1] = 'cass'
# peoplenames[2]= 'sarah'
# peoplenames[3] = 'ellie'
# peoplenames[4] = 'maddy'

# print(peoplenames)


#TASK 3
#given a list of tuples, create a dictionary where the key is the first value in the tuple and the value is the second
#ie. after adding the first item the dictionary would look like this: 
#('chloe': 'wears glasses')
# a_list_of_tuples = [
#     ('chloe', 'wears glasses'),
#     ('maddy', 'is sitting next to beverly'),
#     ('cass', 'is online'), 
#     ('marc', 'is mentoring')
# ]

# tuplelist = {}

# for tuplelist in a_list_of_tuples: 
#     print ('{key} : {value}'.format(
#         key=tuplelist[0],
#         value=tuplelist[1]
#         )
#     )

# Task 4:
# given a list of typles, create a dictionary of dictionaries
# where the first value in the tuple is the key a dictionary
# containing the second value in the tuple is the value for a
# 'description' key in the dictionary
# i.e. after adding the first item the dictionary would look like this:
# result = {
#     'chloe': {
#         'description': 'wears glasses'
#     }
# }

a_list_of_tuples = [
    ('chloe', 'wears glasses'),
    ('maddy', 'is sitting next to beverly'),
    ('cass', 'is online'), 
    ('marc', 'is mentoring')
]

people = {
  description = {}  
}


people['chloe']

for people in a_list_of_tuples:
    print('{key} : {value}'.format(
        key=people
        value=description
    )
