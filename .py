n = input()

def multiplication(*numbers):
    total = 1
    for num in numbers:
        total *= num
    return total
    
print(multiplication(n))