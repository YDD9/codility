"""
A non-empty zero-indexed array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

def solution(A)
that, given a non-empty zero-indexed array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
"""

def solution(A):
"""
Starting from the array's index 0, namely the first car, we have to check its direction:
- if a[0] == 0, car is going to east: increment the count of cars going to east by 1; else, count still is zero;
- starting from next element a[1] until the end of the array, we keep incrementing the count of east-directed cars (a[n] == 0) until we meet a west-directed car. In that case, all the east-directed cars seen before will cross the current west-directed one, so we just multiply east * 1 and add the result to the total amount of passing cars. But as rightly Pasban pointed out to me, east * 1 = east, so we just add the east amount to the passing cars one. Starting from now, if we meet east-directed cars, just increment again the related count; otherwise, we have to increase again the passingCars amount by the amount of all the east-directed cars met before.
"""
    # write your code in Python 2.7
    east = 0 
    passingcars = 0
    for i in range(len(A)):
        if A[i] == 0:
            east += 1
        else:
            passingcars += east
            if passingcars >= 1000000000:
                passingcars = -1
    return passingcars
    

