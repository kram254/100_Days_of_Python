"""
##Operators

Operators are used to perform operations on variables in Python. We have:
Arithmetic Operators
Assignment Operators
Comparison Operators
Logical Operators
"""

## Arithmetic operators
"""
Arithmetic operators are used to perform mathematical operations on numerical variables such as int or float. See the table for the common arithmetic operators used in Python:

Operator	Name of Operation	 Example	Description
+	        Addition	          x + y	    x plus y
-	        Subtraction	          x - y	    x minus y
*	        Multiplication	      x * y	    x multiplied by y
**	        Exponentiation	      x ** y	x raised to the power of y
/	        Division	          x / y  	x divided by y
//	        Floor Division	      x // y	x divided by y, returning integer
%	        Modulo	              x % y	    The remainder of x divided by y

"""
## Examples

x = 4
y = 3
 
x + y  # returns 7
x - y  # returns 1
x * y  # returns 12
x ** y # returns 64
x / y  # returns 1.333
x // y # returns 1
x % y # returns 1

## Assignment Operators
"""
Assignment Operators
There are two types of assignment operators: the assignment operator and compound assignment operators. The assignment operator, =, is used to assign values to variables. Compound assignment operators are used to perform arithmetic operations on a variable and reassign its value at the same time. Here are the common assignment operators:

Operator	Example	     Description
=	        x = 4	      Assign 4 to x
+=	        x += 4	      Add 4 to existing value of x
-=	        x -= 4	      Subtract 4 from existing value of x
*=	        x *= 4	      Multiply existing value by 4
/=	        x /= 4	      Divide existing value by 4
%=	        x %= 4	      Modulo existing value by 4

"""
x = 4

x += 4  # x is 8
x -= 4  # x is 0
x *= 4  # x is 16
x /= 4  # x is 1.0
x %= 4  # x is 0

## Logical Operrators
"""
Comparison Operators
Comparison operators are used to compare two variables. The result from these operators is a bool (True or False). Here are the comparison operators:

Operator	Description	                Example
==	        Equal to	                x == y
!=	        Not equal to	            x != y
>	        Greater than	            x > y
<	        Less than	                x < y
>=	        Greater than or equal to	x >= y
<=	        Less than or equal to	    x <= y
"""

x = 4
y = 3
 
x == y # returns False
x != y # returns True
x > y  # returns True
x < y  # returns False
x >= y # returns True
x <= y # returns False

## Logical Operators
"""
Logical Operators
Logical operators are used to combine and evaluate multiple conditions. The result is a bool (True or False).

Operator	 Description	                                     Example
and	        If both statements are true, returns True	         x > 2 and y > 1
or	        If one of the statements are true, returns True      x > 3 or y > 5
not	        If used, returns the reverse of the actual result	 not(x > 10 and y > 5)
"""

x = 4
y = 3
 
x > 2 and y > 1      # returns True
x > 5 or y <= 3      # returns True
not(x > 2 and y > 1) # returns False
