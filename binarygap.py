"""
N is an integer number.
Converted into binarystring using bin()
Leading and Tailing 0s removed using strip()
String split into groups of 0s using split()
New array of sizes of 0 groups
Returned maximum size of group
"""
def solution(N):
    binary = bin(N)[2:].strip("0").split("1")
    size = [len(i) for i in binary]
    return max(size)

