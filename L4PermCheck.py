# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    
    xorSum = 0
    for i in range(1,N+1):
        xorSum ^= i ^ A[i-1]
    
    if xorSum == 0:
        return 1
    else:
        return 0
        
