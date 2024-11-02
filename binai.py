n = int(input())
a = input()
b = input()

ghalat = 0
for i in range(n):
    if a[i] != b[i]:
        ghalat += 1

print(ghalat)