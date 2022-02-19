"""
PopandSwap:
A is provided array, K is amount of swaps.
For each swap, pops off the last value in the list using pop()
Inserts the popped value on to the front of the list.
Does this for amount of swaps requested.
If the array is empty, pop function doesn't work, so just returns empty list.
"""
def solution(A, K):
    if len(A) != 0:
        for i in range(K):
            move = A.pop()
            A.insert(0,move)
        return A
    else:
        return A
