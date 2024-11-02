n = int(input())

i = 0
m = 0
first = int(input())

while i<(n-1):
    a = int(input())
    if first != i:
        m += 1
        first = a
        i += 1
        
print(m)