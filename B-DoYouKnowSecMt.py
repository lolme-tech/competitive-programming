#https://atcoder.jp/contests/abc201/tasks/abc201_b
N = int(input())
mountain = []
for n in range(N):
    S, T = map(str, input(). split())
    T = int(T)
    mountain.append([S, T])
mountain.sort(reverse = True, key = lambda x:x[1])
print(mountain[1][0])