n=input()
person_1 = input().split()
n=input()
person_2 = input().split()
n=input()
person_3 = input().split()

days = ['shanbe','1shanbe','2shanbe','3shanbe','4shanbe','5shanbe','jome']

count = 0
for day in days:
    if day not in person_1 and \
        day not in person_2 and day not in person_3:
        count +=1

print(count)