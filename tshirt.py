n = int(input())
sum = 0
list_1 = list(input().split())
list_2 = list(input().split())
for i in range(n):
    sum += (int(list_1[i]))*(int(list_2[i]))
print(sum)