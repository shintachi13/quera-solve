name = input()
horof_seda=["a","e","i","o","u"]

total=1

for n in name:
    if n in horof_seda:
        total*=2

print(total)