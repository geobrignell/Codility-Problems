# LBG-practises
Code from the exercises on Codility

Exercises: 
1 - binarygap.py :
    Provided with a number, converts it to binary and returns the maximum gap of zeros.
    Inputs : integer number.
    Returns : Largest zero gap.
    Example : 9 -> 1001, returns 2. 
            : 1045 -> 10000010101, returns 5.

2 - popandswap.py :
    Takes a list and switches all the positions one to the right. 
    Inputs : A, Array. K, Number of swaps.
    Returns : New array.
    Example : [1,2,3], 1, returns [3,1,2].
            : [1,2,3], 2, returns [2,3,1].

3 - oddoccurances.py :
    Array with lots of pairs of numbers and one lone number.
    Find's the number without the pair.
    Inputs : A, Odd length Array
    Returns : The number with an odd amount.
    Example : [2,1,2,3,1], returns 3.
            : [7,4,7], returns 4.

4 - frogjump.py :
    Finds the amount of jumps it takes to get from a to b.
    Inputs : X, Starting position. Y, Final postion. D, jump size.
    Returns : Amount of jumps.
    Example : X = 10, Y = 85, D = 30
                -10 + 30 = 40
                -40 + 30 = 70
                -70 + 30 = 100
            returns the amount of jumps, 3.
-By George Brignell-Cash
