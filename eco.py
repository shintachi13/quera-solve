kalame = input()
print(kalame)
for i in range(1,len(kalame)):
    print(kalame[i]*(i+1)+kalame[i+1:])