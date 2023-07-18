#Atcoderの問題文
#https://atcoder.jp/contests/abc199/tasks/abc199_a
A, B, C = map( int, input(). split())

if A*A + B*B < C*C:
    print("yes")
else:
    print("no")