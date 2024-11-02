rezhim = input()

red = rezhim.count('R')
yellow = rezhim.count('Y')
green = rezhim.count('G')

if red >=3 or (red>2 and yellow>=2) or green==0:
    print('nakhor lite')
else:
    print('rahat bash')