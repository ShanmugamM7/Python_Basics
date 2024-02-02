"""
===============================================
Created by
            Shanmugam Machaa [14/07/2023-08:52]
===============================================
>> Inheritance :- The process of inheriting the properties from one class to another class.
>> Child Class (Derived class):- The class which inherits the properties from the other.
>> Parent Class (Base class):- The class from which the properties been inherited.
>> Types of Inheritance:
    1)Single-level Inheritance:-
        The process of a derived class inherits the properties from single parent class.
    2)Multi-level Inheritance:-
        The process of a derived class inherits the properties from the Parent class and 
        in turns it inherits the properties from its parent class.
    3) Hierarchical Inheritance:-
        More than one derived class inherits the properties from one parent class.
    4)Multiple Inheritance:-
        A derived class inherits the properties from more than one parent class.

"""
#creating a class with name Boy
class Boy(object):   #Parent class

    # Default constructor'
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height
