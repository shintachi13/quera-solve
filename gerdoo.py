# name = 'ali'
# family = 'bli'
# print(name+' '+family)


# mydict={
#     'name':'ali',
#     'family':'bli'
# } 


# def showname(firstname, lastname):
#     return firstname+" "+lastname

# showname(name, family)

# print(showname(name, family))
# print(showname(mydict['name'],mydict['family']))

# numbers = range(25)

# def even_nums(numbers):
#     total = 0
#     for num in numbers:
#         if num % 2 == 0:
#             total += 1
#     return total
# print(even_nums(numbers))

# def fullname(first,last):
#     return f'{first} {last}'

# print(fullname(last='bli',first='ali'))

# def sum_num(num1,num2,num3):
#     return num1+num2+num3

# print(sum_num(2,4,6))

# def sum_num(*nums):
#     total = 0
#     for i in nums:
#         total += i
#         return total

# print(sum_num())

# def sui(**kwargs):
#   for key,value in kwargs.items():
#     print(f'{key}:{value}')

# sui(name='ali', family= 'bli')


# def display_info(a,b,*args,defpara='default',**kwargs):
#     return [a,b,args,defpara,kwargs]

# print(display_info(1,2,6,firstname='ali',lastname='bli'))

# numbers = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


# def sum_num(*numbers):
#     total = 0
#     for i in numbers:
#         total += i
#     return total

# print(sum_num(*numbers))

# # print(numbers.__name___)

# sum_2 = lambda first, second: first + second
 
# print(sum_2(4+4,5))



name = ('ali','bli')
resualt = name.title()
print(resualt)