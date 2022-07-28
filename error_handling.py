"""
error handling refers to the process of anticipating and resolving errors when they arise. Error handling allows for flexibility 
in the code as it executes different blocks of code based on the presence of errors.

try and except
The clause try attempts to execute a block of code and except executes another block of code if try fails.

"""

nums = [0, 1, 2, 3]
 
try:
   print(sum(nums))
 
except:
   print('Cannot print the sum! Your variables are not numbers.')

"""
The try clause above tries to execute the code print(sum(nums)) to print the sum of the list nums. Because nums is a list of integers, 
the try clause will successfully run the code print(sum(nums)) which will result in the following output:

"6"
In a case where the try clause runs into an error, the code under except will be executed instead.

"""

nums = ['x', 'y', 'z']
 
try:
   print(sum(nums))
 
except:
   print('Cannot print the sum! Your variables are not numbers.')

"""
The try clause above will fail because the list nums has strings, which cannot be added together with sum(). Instead, the code under 
except will be executed:

"Cannot print the sum! Your variables are not numbers."

finally
The finally clause executes a block of code regardless of which clause, try or except, was executed. The finally clause is useful in 
cases where both of your try and except might fail.

"""
nums = ['x', 'y', 'z']
 
try:
   print(sum(nums))
 
except:
   print('Cannot print the sum! Your variables are not numbers.')
 
finally:
   print('Hope you got the result you want!')

"""
The code above will print the following:

Cannot print the sum! Your variables are not numbers.
Hope you got the result you want!
"""