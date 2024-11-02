n = list(input())
n = list(map(int,n))
n = str(sum(n))

while len(n) !=1:
    n= list(map(int,n))
    n= str(sum(n))


print(int(n))