n = int(input())

for i in range(n +1):
    tavan =2 ** i

    if tavan > n:
        print(2 ** i)
        break