# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, A):
    # write your code in Python 2.7

    def firstNum(A, num):
        result = None
        for i in range(len(A)):
            if A[i] == num:
                result = i
                return result
        if result == None:
            return -1

    max = 0
    for j in range(1, X + 1):
        cur = firstNum(A, j)
        if cur >= max:
            max = cur
        if cur == -1:
            return -1
    return max

print solution(3, [3])