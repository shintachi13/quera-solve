n,k = [int(i) for i in input().split()]


nobat = 1
count = 1
while True:
    nobat += k
    nobat = (nobat - n) if nobat > n else nobat

    if nobat == 1:
        break
    count += 1

print(count)