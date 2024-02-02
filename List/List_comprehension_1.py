"""
================================================
Created by 
        Shanmugam Machaa[15/07/2023-23:30]
================================================
"""
# Creating a list of Tuples from two separate Lists
Bike = ["Pulsar", "Cd 100", "XL 100"]
Gears = [5,4,0]
Details = [(name, gear) for name, gear in zip(Bike, Gears)]
print(Details)