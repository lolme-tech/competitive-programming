#https://atcoder.jp/contests/abc188/tasks/abc188_b
N = int(input())
A = list(map( int, input(). split()))
B = list(map( int, input(). split()))

ANS = 0
for i in range(N):
   ANS += A[i]*B[i]
if ANS == 0:
   print("yes")
else:
   print("no")