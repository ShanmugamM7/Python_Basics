"""
================================================
Created by
    Shanmugam Machaa [17/07/2023-17:04]
================================================

>> reduce function:- The reduce function is a higher order function in which it applies a function to first two elements of the iterable and
                     to the result and the next element and so on, until a single value is obtained.
                     Syntax:-
                    Before python 3.9:- reduce(function, iterable[,initialization])
                    python 3.9 onwards:- functools.reduce(function, iterable[,initialization])
"""
from functools import reduce
# reduce function to sum all the elements in the list
list_1 = [1, 2, 3, 4, 5]
sum_out = reduce(lambda x,y: x+y, list_1)
# sum_out_1 = reduce(lambda x,y: x+y, list_1, 10) # Output>> 25
print(sum_out) # Output>> 15

# reduce function to find product of all the elements in the list
prod = reduce(lambda x,y: x*y, list_1)
prod_1 = reduce(lambda x,y: x*y, list_1,10) # Output>> 1200
print(prod) # Output>> 120

# reduce function to concatenate strings
string = ["This ", "is ", "my ", "code."]
word = reduce(lambda x,y: x+y, string)
print(word) # Output>> This is my code.
