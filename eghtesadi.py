n, k = [int(i) for i in input().split()]
string = [int(i) for i in input().split()]
sums = sum(string)

print(n - (- (-sums // k)))