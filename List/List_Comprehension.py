"""
================================================
Created by 
        Shanmugam Machaa[15/07/2023-11:42]
================================================
>> List Comprehension :- It is the  concise and powerful way to create lists from exist lists or other iterable items.

"""

#using list comprehension
numbers = [1,2,3,4,5,6,7,8,9]

even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers using list comprehension:- {}".format(even_numbers))

odd_numbers = [num for num in numbers if num % 2 != 0]
print("Odd numbers using list comprehension:- {}".format(odd_numbers))

#without list comprehension
l=[]
for num in numbers:
    if num%2 == 0:
        l.append(num)
print("Even numbers without using list comprehsion:- {}".format(l))

#nested list to demonstrate list comprehension
matrix = [[1,2,3], [4,5,6], [7,8,9]]
list_form = [num for items in matrix for num in items] # to flatten
print("list_form = ",list_form) 

#creating a matrix
matrix1 = [[j for j in range(3)]for i in range(3)]
print("matrix1 = ",matrix1) 

#Squares
squares = [x**2 for x in range(1,9)]
print("squares = ",squares)

# reversing each string in a list 
s_list = [string[::-1] for string in ["this", "is", "going", "to", "reverse"]]
print(s_list) 