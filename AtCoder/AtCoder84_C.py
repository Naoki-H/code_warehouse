from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)
C = sorted(C)

score = 0
for numB in B:
    numA = bisect_left(A,numB)
    numC = len(C) - bisect_left(C,numB + 1)
    score += numA * numC


print(score)



