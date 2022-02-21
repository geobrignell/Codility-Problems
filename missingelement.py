"""
MissingElement is a function which finds the missing number of an array.
The array contains integers in a range [1,...,(N+1)] where N is the length of the array.


This function works using some properties of the XoR binary function.
The properties are that n ^ n = 0 and n ^ 0 = n.

Since we are couting from 1-N+1, the array is very simular to it's index.
By adding 1 onto the index. We get the same array, except with the missing element and
without the last value in the array.

We therefore need to cancel out the final value of the array. This will be equivilent to
the length of the array + 1. 
Therefore start the loop with this value.
As the loop runs, the numbers all cancel with their index, apart from the number that's missing.
Therefore are left with n ^ 0 where n is the number that is missing.

Example : A = [1,2,3,4,6]
        : index + 1 = [1,2,3,4,5]
        : 6 ^ 1 ^ 1 ^ 2 ^ 2 ^ 3 ^ 3 ^ 4 ^ 4 ^ 5 ^ 6 = 6 ^ 0 ^ 0 ^ 0 ^ 0 ^ 5 ^ 6
        : = 6 ^ 6 ^ 5 = 0 ^ 5 = 5
        : returns 5
"""

def solution(A):
    value = len(A) + 1
    for idx, num in enumerate(A):
        
        value = num ^ (idx+1) ^ value
    return value

