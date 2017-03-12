# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7

    N = len(A)
    X = [0]*N
    sum = 0
    for i in range(N):
        if 0<=A[i]-1<N and X[A[i]-1] == 0:
            X[A[i]-1] = A[i]

    for i in range(N):
        if X[i] == 0:
            return i+1
        else:
            sum += 1

    if sum == N:
        return N+1

    return 1


print solution([1,2,3])