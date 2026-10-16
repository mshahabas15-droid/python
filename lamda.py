# # squire=lambda x:x*x
# # print(squire(5))
# # largest=lambda a,b:a if a>b else b
# # print(largest(10,15))
# # even =lambda a:a%2==0
# # print(even(6))
# # print(even(5))
# # add=lambda a,b:a+b
# # print(add(56,56))

#**************************************************
l=[2,3,4,5,6]
# def cube(a):
#     return a**3

find_cube=list(map(lambda x:x**3,l))
print(find_cube)

# numbers=[1,2,3,4]
# result=list(map(lambda X:X*2,numbers))
# print(result)


 
# # numbers=[1,2,3,4,5,6]
# # result=list(filter(lambda X : X%2==0,numbers))
# # print(result)

from functools import reduce
# # numbers=[1,2,3,4]
# # result=reduce(lambda a,b:a+b,numbers)
# # print(result)

# # a=[2,3,4,5]
# # result=list((map(lambda n:n*n,a)))
# # print(result)

# # a=[2,3,4,5,6]
# # result=list(map(lambda n:n/2,a))
# # print(result)

# n=[2,45,6,78,34]
# result=list(map(lambda x:x<10,n))
# print(result)

# n=[2,3,4,5,6,7]
# result=reduce(lambda a,b:a-b,n)
# print(result)

# a=[1,2,3,4,5]
# b=list(filter(lambda n:n%2==0,a))
# print(b)

