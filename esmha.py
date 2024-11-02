n = int(input())
asami =[]

for  i in range(n):
    asami.append(input())

print(max([len(set(i)) for i in asami]))