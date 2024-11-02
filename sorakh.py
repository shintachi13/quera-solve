n = input().split()
moosh = int(n[0])
soorakh = int(n[1])
if soorakh==moosh:
    print("Saal Noo Mobarak!")

else:
    if moosh>soorakh:
        for i in range((moosh-soorakh)):
            print('L',end='')
            
    else:
        for i in range((soorakh-moosh)):
            print('R',end='')
print()