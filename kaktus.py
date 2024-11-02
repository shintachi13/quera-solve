n = int(input())
group = [int(i) for i in input().split()]


for i in list(group):
    if i<3:
        print('*'*int(i))
    
    elif i == 3:
        print('***')
        
    else:
        print('*')