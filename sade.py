numbers = []
product = 1
for i in range(4):
    n = int(input())
    product *= n
    numbers.append(n)

print(f'Sum : {"%.6f" % sum(numbers)}')
print(f'Average : {"%.6f" % (sum(numbers) / 4)}')
print(f'Product : {"%.6f" % product}')
print(f'MAX : {"%.6f" % max(numbers)}')
print(f'MIN : {"%.6f" % min(numbers)}')