n = None
list1 = []
while n != 0:
    n = int(input())
    list1.append(n)
list1.pop()
list1.reverse()

for i in list1:
    print(i)