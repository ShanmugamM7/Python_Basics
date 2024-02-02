"""
================================================
Created by
    Shanmugam Machaa [13/07/2023-23:37]
================================================

>> Dictionary:- Python Dictionaries are powerful data structures that store data in the form of key-value pair.
                Note:- From 3.7 version, dictionaries are ordered. Earlier of 3.7 dictionaries are unordered.
                Dictionaries are mutable and duplicates are not allowed.
"""
# Creating dictionaries
# Using curly braces
dict_1 = {'a':1, 'b':2, 'c':3, 'd':4}
print(dict_1)

# Using dict()
dict_2 = dict(A = 'Aspire', B = 'Bold', C = 'Competency')
print(dict_2)

# Using a list of tuples
dict_3 = dict([('name', 'Pulsar'),('Gears', 5),('Cost_in_lakhs', 1.5)])
print(dict_3)

# Accessing existing elements
print(dict_3['name'])  # Output>> 'Pulsar'
print(dict_3.get('Gears'))  # Output>> 5

# Accessing non-existing elements
# print(dict_3['Name'])  # Output>> KeyError
print(dict_3.get('gears'))  # Output>> none

# Adding new key-value pair
dict_3['milage'] = 40

# Modifying existing value
dict_3['name'] = 'Apache'
print(dict_3) # Output>> {'name': 'Apache', 'Gears': 5, 'Cost_in_lakhs': 1.5, 'milage': 40}

#Removing key-value pair
# del dict_name[key]: 
del dict_3['Cost_in_lakhs'] 
print(dict_3) # Output>> {'name': 'Apache', 'Gears': 5, 'milage': 40}

# pop(key): Removes the key-value pair and returns the value.
print(dict_3.pop('Gears')) # Output>> 5
print(dict_3) # Output>> {'name': 'Apache', 'milage': 40}

# Methods
dict_4 = {'name':'Shanmugam', 'age':22, 'Qualification':'B.Tech', 'height':5.8}
keys = dict_4.keys() # to get list of all the keys
print(keys) # Output>> {'name': 'Apache', 'milage': 40}

values = dict_4.values() # to ger list of all the values
print(values) # Output>> dict_values(['Shanmugam', 22, 'B.Tech', 5.8])

items = dict_4.items() # to get key-value pait in a tuple belongs to list
print(items) # Output>> dict_items([('name', 'Shanmugam'), ('age', 22), ('Qualification', 'B.Tech'), ('height', 5.8)])

