"""
for loops
The for loop is used to iterate over items and execute code on each item. It has two keywords, for and in, which are used to describe 
the element and the object that is being iterated over, respectively. The indentation after : starts the body of the loop.

In the example below, the for loop is iterating over the list nums. For each item in num, it is printing the output of num + 1.
"""
from doctest import Example


nums = [1, 2, 3, 4, 5]
 
for num in nums:
   print(num + 1)
##This will output:

2
3
4
5
6



"""
for loops with range()
The range() function can be used with the for loop to execute a block of code multiple times. The code below iterates between 
numbers 0 to 2 and prints each number.

"""
for i in range(3):
   print(i)



"""
Nested for loops
A for loop can have nested for loops. This is particularly useful if the items you are iterating over contain subitems. In the example 
below, we have a list of lists called teams and we can use a nested for loop to print each name in the lists.
"""
teams = [['Jody', 'Abe'], ['Abhishek', 'Kim'], ['Taylor', 'Jen']]
for team in teams:
   for name in team:
       print(name)




"""
while loops
The while loop is used to execute code until the condition evaluates to be True. In the example below, the while loop will run and 
print i until the value of i is less than 6.
"""
i = 1
while i < 6:
    print(i)
    i += 1

## Example
# for loop
num = [4, 5, 16]

print("For loops example")

for num in nums:
    print(num ** 2)

# while loop
i = 3

print("While loops example")

while i < 256:
    print(i)
    i = i ** 2