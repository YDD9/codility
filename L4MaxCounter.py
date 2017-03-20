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

## I think i picked up some ideas from other languages, find my solution. The key is not to iterate/create new array of results in the loop over A. just keep track of the last maximum. only AFTER the loop completes - adjust values less than last maximum - with the last maximum. Lazy-write algo.

# https://codesays.com/2014/solution-to-max-counters-by-codility/

def solution(N, A):
    result = [0]*N    # The list to be returned
    max_counter = 0   # The used value in previous max_counter command
    current_max = 0   # The current maximum value of any counter

    for command in A:
        if 1 <= command <= N:
            # increase(X) command
            if max_counter > result[command-1]:
                # lazy write
                result[command-1] = max_counter
            result[command-1] += 1
            if current_max < result[command-1]:
                current_max = result[command-1]
        else:
            # max_counter command
            # just record the current maximum value for later write
            max_counter = current_max

    for index in range(0,N):
        if result[index] < max_counter:
            # This element has never been used/updated after previous
            #     max_counter command
            result[index] = max_counter

    return result
