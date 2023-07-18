"""
================================================
Created by 
        Shanmugam Machaa[15/07/2023-11:42]
================================================
>> 

"""
# append(element): Adds an element to the end of the list.
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output>> [1, 2, 3, 4]

# extend(iterable): Adds elements of the iterable at the end of the list.
my_list = [1, 2, 3]
my_list.extend([4, 5, 6]) 
print(my_list) # Output>> [1, 2, 3, 4, 5, 6]

# insert(index, element): Inserts the element at specified index.
my_list = [1, 2, 4, 5]
my_list.insert(2,3)
print(my_list) # Output>> [1, 2, 3, 4, 5]

# remove(element): Remove the first occurrence of the element.
my_list = [1, 2, 3, 4, 4, 5]
my_list.remove(4)
print(my_list) # Output>> [1, 2, 3, 4, 5]

# pop(index): Removes and returns the element at specified index. If no index is provided then removes and returns last element.
my_list = [1, 2, 3, 4, 9, 5, 6]
my_list.pop(4)
print(my_list) # Output>> [1, 2, 3, 4, 5, 6]

# index(element): Returns the index of the first occurrence of the specified element.
my_list = [1, 2, 3, 4, 5]
print(my_list.index(3)) # Output>> 2

# count(element): Returns the number of occurrences of the specified element.
my_list = ['q', 'e', 'd', 'e', 'r', 'e']
print(my_list.count('e')) # Output>> 3

#reverse(): Reverses the order of the elements in the list
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list) # Output>> [5, 4, 3, 2, 1]

# copy(): Returns a shallow copy of the list
my_list = [1, 2, 3, 4, 5]
list_copy = my_list.copy()
print(list_copy) # Output>> [1, 2, 3, 4, 5]

# clear(): Removes all the elements of the list
my_list = [1, 4, 5, 9]
my_list.clear()
print(my_list) # Output>> []