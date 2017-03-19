def solution(N, A):
    # write your code in Python 2.7
    M = len(A)
    res = [0] * N
    maxcount = 0
    oldmaxcount = 0
    for K in range(M):
        if 1 <= A[K] <= N:
            res[A[K]-1] += 1
            if res[A[K]-1] >= maxcount:
                oldmaxcount, maxcount = maxcount, res[A[K]-1]                
        if A[K] == N + 1 and oldmaxcount != maxcount:
            res = [maxcount] * N
    return res

## t's O(N*M) - in extreme test they are doing N times max operation, so each time you're filling array with maxValue (M elements each time * N times)

## add oldmaxcount, if oldmaxcount == maxcount, no new res will be created.

## I think i picked up some ideas from other languages, find my solution. The key is not to iterate/create new array of results in the loop over A. just keep track of the last maximum. only AFTER the loop completes - adjust values less than last maximum - with the last maximum

def solution(N, A):
    # write your code in Python 2.7
    M = len(A)
    res = [0] * N
    maxcount = 0
    sumcount = 0
    for K in range(M):
        if 1 <= A[K] <= N:
            res[A[K]-1] += 1
            if res[A[K]-1] >= maxcount:
                maxcount = res[A[K]-1]                
        if A[K] == N + 1:
            sumcount += maxcount 
    return res + [sumcount] * N
