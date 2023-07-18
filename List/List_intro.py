"""
================================================
Created by
    Shanmugam Machaa [13/07/2023-23:37]
================================================
>> List:- List is a versatile data type in python that can store data of any type. 
          It is order with the index numbers through which we can do certain operations like
          accessing elements, replacing, deleting or adding elements and slicing etc.
          Lists in python are mutable means one can able to alter the elements in it.

>> Index:- The serial notation of the elements in a list starts with 0.  
           The index numbers starts from 0 and ends with lenght(object)-1.  
           Negative indexing -1 represents the last element of the list and 
           -(length(object)) represents the first element of the list.
   
        Example:-
            my_list = ['a', 'b', 'c', 'd', 'e'] 
            index num   0    1    2    3    4
        Negetive index   -5   -4   -3   -2   -1
        
>> Slicing:- Used to get a portion of list by providing the start and ending index(excluded) along with step size if requires.
            list_name[start:end:step] # all the parameters are optional
            The end index is excluded here.
        Example:-
            my_list[4:9] # it will slice my_list from index number 4 to index number 8.
            
"""

# creating a list 
empty_list =[]   # creating empty list
list_1 = [1,2,'a',2.14, "my list",'!'] # initialized with elements
print(list_1)
# Accessing elements through indices starts with 0
print(list_1[2]) # to access 'a' in list_1, the index is 2
print(list_1[0]) # to access first element from list_1
# To access the last element of list_1
print(list_1[-1]) # using negative indexing
print(list_1[len(list_1)-1]) # if we don,t know the last index number
print(list_1[5]) # using the last index number


# To modify elements in the list
list_1[5] = '@'
print(list_1)

# List slicing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#+ve index 0  1  2  3  4  5  6  7  8  9
#-ve      -9 -8 -7 -6 -5 -4 -3 -2 -1  0

# with positive index
slice_1 = numbers[3:8] # slices from index 3 to index 7
slice_2 = numbers[:6] # slices from the start to index 5
slice_3 = numbers[3:] # slices from index 3 to the last
slice_4 = numbers[:] # all the list elements
slice_5 = numbers[2:10:2] # slices from index 2 to index 9 with step of 2

# with negative index
slice_6 = numbers[:-1] # slicing upto last second element 
slice_7 = numbers[-3:] # last three elements
slice_8 = numbers[-6:-1] # from negative index -6 to -2
# to convert -ve index to positive index (length(list)+negetive_index-1)
slice_9 = numbers[::-1] # Reversing the list

# Modifying multiple elements in the list using slice
numbers[0:5] = [11, 12, 13, 14, 15] # output>> numbers = [11, 12, 13, 14, 15, 6, 7, 8, 9, 10]

# Adding elements to the list
my_list = [1,2,4] 
my_list.append(5) # add the given element at the last. Output>> [1, 2, 4, 5]
my_list.insert(2,3) # inserts 3 at index number 2. Output>> [1, 2, 3, 4, 5]

# Removing elements from the list
list_2 = [0,1,2,3,8,4,5,7]
list_2.remove(7) # Removes a specific element: 7 get removed
del list_2[4] # Removes element at a specified index: element at index 4 get removed

# List concatenation
l1 = [0,1,2]
l2 = [3,4,5]
l3 = l1+l2  # new list with l1 and l2 elements. output>> [0, 1, 2, 3, 4, 5]

# list length
length = len(l3) # output>> 6

#list Sorting
list_3 = [3,2,4,1,7,0,9]
# Changes the original list itself
# Sorting the list in ascending order. 
list_3.sort() # output>> [0, 1, 2, 3, 5, 7, 9]

# Sorting the list in descending order.
list_4 = [0,3,5,4,1,2] 
list_4.sort(reverse = True) # output>> [5, 4, 3, 2, 1, 0]



