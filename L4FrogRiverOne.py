# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

## firstNum return when a given num first appears in A
## find each step from 1 to X when their first appearance is and count +1 if their appearance is found
## save their max time to appear and return max time only when count reaches X
## O(N**2) time complexity

# def solution(X, A):
#     # write your code in Python 2.7
#
#     def firstNum(A, num):
#         result = None
#         for i in range(len(A)):
#             if A[i] == num:
#                 result = i
#                 return result
#         if result == None:
#             return -1
#
#     max = 0
#     for j in range(1, X + 1):
#         cur = firstNum(A, j)
#         if cur >= max:
#             max = cur
#         if cur == -1:
#             return -1
#     return max


## Create a X length array: all elements are 0.
## Iterate the A array: if current A value, index for X, has not been found before, then
## add the value 1 to the element at the corresponding index and add one to a sum variable.
## When X and sum are equal, all leaves are in place.

def solution(X, A):
    listX = [0] * X
    sum = 0
    for i in range(len(A)):
        if A[i]<=X and listX[A[i]-1] == 0:
            listX[A[i]-1] = A[i]
            sum += 1
        if sum == X:
            return i
    return -1




print solution(3, [1,26,7,2])