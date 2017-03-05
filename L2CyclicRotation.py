def solution(A, K):
    n = len(A)
    if n==0 or n==1:
        return A

    K = K % n
    if K <= 0:
        return A
    else:
        return A[-K:] + A[: (n-K)]


print solution([0,9] ,2)