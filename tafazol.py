n = (input())

def game(number):
    num = str(number)

    if (num[1] > num[0]):
        result = int(num[1]) - int(num[0])

    elif (num[1] < num[0]):
        result = int(num[0]) - int(num[1])

    else:
        result = 0
    return result


print(game(n))