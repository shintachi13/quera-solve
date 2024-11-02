num = input().split()
a , b , l = int(num[0]),int(num[1]),int(num[2])
count = 1
sum = 0
while count<=1:
    if count % 2 !=0:
        sum += a
    else:
        sum += b
    count +=1
print(sum)