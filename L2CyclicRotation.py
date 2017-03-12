def solution(A, K):
    n = len(A)
    if n==0 or n==1:
        return A

    if K <= 0:
        K = K % n

        return A
    else:
        return A[-K:] + A[: (n-K)]


print solution([0,9] ,2)
