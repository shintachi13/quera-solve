a, b = [int(i) for i in input().split()]
b = "00" if b == 0 else str(60 - b)
a = "00" if a == 0 else str(12 - a)

if len(b) < 2:
    b = "0" + b

if len(a) < 2:
    a = "0" + a

print(f'{a}:{b}')