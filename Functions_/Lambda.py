"""
================================================
Created by 
        Shanmugam Machaa[16/07/2023-10:50]
================================================
>> Lambda Function:- Also known as anonymous functions which are small, inline functions that do not have any name.
                General Syntax:-    lambda argument: expression
                Lambda function is used in such a situation where we need a simple function in which the context does
                not require any separate definition.
                Lambda functions are often used along with the higher order functions like map, filter and reduce.

>> Map Function:- The map function applies a function over each item of an iterable and returns an iterator with results.
                General Syntax:- map(function, iterable)

>> Filter Function:- Filter function creates a iterator over the elements of a iterable in which the given function returns True. 
                    Lambda function can be used to define filter function.
                General Syntax:- filter(function, iterable)
>> Difference between filter and map functions:- The filter function is used to selectively include elements based on a condition, 
                                                 while the map function is used to transform each element using a function.

            
"""
# Square of a number using lambda function
square = lambda num: num**2
print(square(5)) # Output>> 25

# Map function along with lambda
numbers = [1, 2, 3, 4, 5, 6]
double = map(lambda num: num*2, numbers)
print(list(double)) # Output>> [2, 4, 6, 8, 10, 12]

# Map function to convert string numbers to integer numbers
numbers = ['1', '2', '3', '4', '5']
num = map(int,numbers)
print(list(num)) # Output>> [1, 2, 3, 4, 5]

# Map function to make all letters of each string in a list to upper case
string = ['Rama', 'siva', 'Laxmana', 'Arjuna']
upper_str = map(str.upper, string)
print(list(upper_str)) # Output>> ['RAMA', 'SIVA', 'LAXMANA', 'ARJUNA']

# map function using function composition: using multiple functions
numbers = [1, 2, 3, 4]
output = map(lambda x: x+1,map(lambda num:num**2,numbers))
print(list(output)) # Output>> [2, 5, 10, 17]

# Filter function along with lambda
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x%2 == 0, numbers)
print(list(even_numbers)) # Output>> [2, 4, 6]

# filter function example
values = [0, False, 'Shanmugam', 1, 43.79, 'True', ""]
non_empty = filter(bool,values)
print(list(non_empty)) # Output>> ['Shanmugam', 1, 43.79, 'True']


# Sort: Used to sort an iterable by a specified key. Lambda can be used to define key to sort the iterable.
Bikes = ['Pulsar', 'Xtreme', 'Splendor', 'Sport', 'CD100', 'Duke']
# sort() with no arguments returns sorted list according to alphabetical order
# Bikes.sort() # Output>> ['CD100', 'Duke', 'Pulsar', 'Splendor', 'Sport', 'Xtreme']
Bikes.sort(key=lambda x: len(x))
print(Bikes) # Output>> ['Duke', 'Sport', 'CD100', 'Pulsar', 'Xtreme', 'Splendor']


























