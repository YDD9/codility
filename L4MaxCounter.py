def solution(N, A):
    # write your code in Python 2.7
    M = len(A)
    res = [0] * N
    for K in range(M):
        if 1 <= A[K] <= N:
            res[A[K]-1] += 1
        if A[K] == N + 1:
            res = [max(res)] * N
    return res
