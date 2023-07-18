#https://atcoder.jp/contests/abc190/tasks/abc190_b
N, S, D = map(int, input(). split())
ANS = False
for n in range(N):
    X, Y = map(int, input(). split())
    if X < S and Y > D:
        ANS = True
if ANS == True:
    print("yes")
else:
    print("no")