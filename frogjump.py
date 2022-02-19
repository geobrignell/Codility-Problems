"""
Works out how many jumps it takes to get from a -> b.
X - inital position
Y - final position
D - jump distance
Assumption X <= Y

Example :  X = 10, Y = 85, D = 30
-10 + 30 = 40
-40 + 30 = 70
-70 + 30 = 100
returns 3 as thats how many jumps it took.
"""

def solution(X,Y,D):
    if X == Y:
        return 0
    distance = Y - X
    if distance%D:
        return distance//D + 1
    else:
        return distance/D    
