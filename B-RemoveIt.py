#https://atcoder.jp/contests/abc191/tasks/abc191_b
N, X = map( int, input(). split())
A = list(map( int, input(). split()))
ANS = []
for i in range(N):
    if A[i]!=X:
        ANS.append(A[i])
print(ANS)