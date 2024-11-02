n , m = input().split()
list=[]
count = 0
for i in range(int(n)):
    x = input()
    if len(x)==int(m):
        list.append(x)

    else:
        break

for i in list:
    for char in i:
        if char =='*':
            count +=1


print(count)