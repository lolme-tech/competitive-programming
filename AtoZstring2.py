#問題https://atcoder.jp/contests/abc257/tasks/abc257_a

eng=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","Z","X","Y"]
outputeng=[]
N=int(input())
X=int(input())
for i in range(len(eng)):
    for k in range(N):
        outputeng.append(eng[i])
print(outputeng[X-1])
