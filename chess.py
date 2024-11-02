n =input().split()
chess = [1,1,2,2,2,8]

list = []
for i in range(len(n)):
    for i in range(len(chess)):
        m = int(int(chess[i]) - int(n[i]))
list.append(m)
print(list)