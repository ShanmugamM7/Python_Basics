"""
================================================
Created by 
        Shanmugam Machaa[16/07/2023-02:11]
================================================

>> Shallow copy:- It creates the copy from the original object along with the reference of the nested objects present in the original object.
                The top-level  objects are duplicated and are independent. 
                But the nested objects are still shared between both original and copied objects. 
                Modification of nested object either in original or in copy objects will reflect in both the objects.
                Shallow copy can be created by copy() method with no arguments.

>> Deep copy:- It creates the copy from the original object along the nested objects present in the original object.
                The top-level objects and nested objects both are duplicated and resulting in two independent and separate objects.
                Modification of nested object either in original or in copy objects will not reflect the object.
                Deep copy can be created by copy,deepcopy() function from copy module.
"""
import copy # for Deep copy demo

#Shallow copy demo
original = [1, 2, 3, [4, 5, 6], 7, 8]
shallow = original.copy()
print(original) # Output>> [1, 2, 3, [4, 5, 6], 7, 8]
print(shallow)  # Output>> [1, 2, 3, [4, 5, 6], 7, 8]
shallow[3][0] = 0
original[3][2] = 16
shallow[1] = 9
original[0] = 11
print(original) #Output>> [11, 2, 3, [0, 5, 16], 7, 8]
print(shallow)  #Output>> [1, 9, 3, [0, 5, 16], 7, 8]

#Deep copy demo
original = [1, 2, 3, [4, 5, 6], 7, 8]
deep = copy.deepcopy(original)
print(original) # Output>> [1, 2, 3, [4, 5, 6], 7, 8]
print(deep)     # Output>> [1, 2, 3, [4, 5, 6], 7, 8]
deep[3][0] = 0
deep[1] = 9
original[0] = 11
original[3][2] = 16
print(original) # Output>> [11, 2, 3, [4, 5, 16], 7, 8]
print(deep)     # Output>> [1, 9, 3, [0, 5, 6], 7, 8]