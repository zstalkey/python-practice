# given a list of names, use a loop to create a dictionary where each entry has a "name" key, with the name from the list as the value


people = {}
# print(people)

people = {
    'hayley': 'lead instructor',
    'nanwen': 'wears checkered shirts'
}
# print(people)

people['chloe'] = 'wears glasses'
people['hayley'] = 'is wearing red'

# print(people)
# print(people['chloe'])

# Task 1: use a for loop to print out each key and value in a dict

for person in people:
    print(person)

for person in people:
    print('{key}: {value}'.format(
        key=person,
        value=people[person]
        )
    )


names = ['chloe', 'cass', 'sarah', 'ellie', 'maddy']

# Task 2: given a list of names, create a dictionary where the key
# is the index and the value is the name, i.e. after adding
# the first name the dictionary would look like this:
# {0: 'chloe'}

a_list_of_tuples = [
    ('chloe', 'wears glasses'),
    ('maddy', 'is sitting next to beverly'),
    ('cass', 'is online'),
    ('marc', 'is mentoring')
]

# Task 3:
# given a list of tuples, create a dictionary where the key
# is the first value in the tuple and the value is the second,
# i.e. after adding the first item the dictionary would look like this:
# {'chloe': 'wears glasses'}

# Task 4:
# given a list of typles, create a dictionary of dictionaries
# where the first value in the tuple is the key a dictionary
# containing the second value in the tuple is the value for a
# 'description' key in the dictionary
# i.e. after adding the first item the dictionary would look like this:
result = {
    'chloe': {
        'description': 'wears glasses'
    }
}
