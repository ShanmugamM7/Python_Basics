"""
===========================================
Created by
        Shanmugam Machaa[15/07/2023-19:09]
===========================================
"""
import time

# function to double the elements in a list using for loop
def In_loop(n):
    l = []
    for number in n:
        l.append(number*2)
    return l

# function to double the elements in a list using list comprehension
def List_comprehension(n):
    return [num*2 for num in n]

numbers = [j for j in range(1000000)]

start = time.time()
In_loop(numbers)
end = time.time()
print("Time required for In_loop function: ",round(end-start,4))

start = time.time()
List_comprehension(numbers)
end = time.time()
print("Time required for List_comprehension function: ",round(end-start,4))
