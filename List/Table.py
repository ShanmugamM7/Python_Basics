"""
================================================
Created by 
        Shanmugam Machaa[15/07/2023-21:28]
================================================
"""
# Using loop to print 20 table
tab = []
for i in range(1,11):
    tab.append(10*i)
print(tab)

# Using list comprehension
tab = [num*10 for num in range(1,11)]
print(tab)

# Using list comprehension along with lambda function
tab = list(map(lambda i: i*10, [i for i in range(1,11)]))
print(tab)
