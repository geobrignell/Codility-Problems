"""
A is a non zero array with an odd length.
It contains many pairs of numbers with one alone.
The function takes the array and returns the solo number.
First if, if the length of the array is one, the number must be the solo number.
So the first and only number in the array is returned.
The array is sorted. This puts the pairs next to eachother.
Using a for loop, jump from 0, in twos, till the odd number is found.
The first if statement, returns the last element if it wasn't identified from the other if loop.
The second if statement, checks each pair, checks that the two numbers are the same. If not,
returns the first number. This works as the array was sorted. So it will always be the first number.
"""
def solution(A):
    if len(A) == 1:
      return A[0]
    A = sorted(A)
    for i in range(0,len(A),2):
      if i+1 == len(A):
        return A[i]
      if A[i] != A[i+1]:
        return A[i]

#Slower intial method.
#Too slow for test.
#checks that there are an even number for each number in the array. Returns the one that isnt.
def solutionslow(A):
    for i in set(A):
        if A.count(i)%2 != 0:
            return i
        

#Amazing binary XOr trick, the binary number kind of stores all the previous numbers,
#when a number acts on it twice, they "cancel" themselves out, the only number that
#doesn't cancel is the one by itself.
#Method using Binary
def solutionbinary(A):
   result = 0
   for number in A:
     result ^= number
   return result


