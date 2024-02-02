"""
================================================
Created by
    Shanmugam Machaa [13/07/2023-23:47]
================================================
>> Class :- Blue print from which the objects get created.
>> Object :- Entity that have attributes(Properties) and Methods(Actions) along with Identity.
>> self :- self and object of a particular class is referred to the same thing.
>> Constructor :- Constructors are used to initialize the values to the data members of the class.
>> __init__ :- a default constructor, it is get activated if the object of the class get created. 
               
"""
#Creating class
class Animal:

    #class attribute
    attr1 = "four legs"

    #Instance attribute
    def __init__(self, name):
        self.name = name
        print("Address of self is ",id(self))
    
    #Method
    def speak(self):
        print("I'm a {}".format(self.name))
#Object instantiation
Dog = Animal("Pandu")
Cat = Animal("Tommy")

# #Accessing class attribure
# print("Dog has {}".format(Dog.__class__.attr1))      # Animal.attr1
# print("Cat has {}".format(Cat.__class__.attr1))

# #Accessing instance attribute
# print("Dog name is {}".format(Dog.name))
# print("Cat name is {}".format(Cat.name))

print("Address of Dog is ",id(Dog))
print("Address of Cat is ",id(Cat))
#Accessing class method
Dog.speak()
Cat.speak()
