# a=int(input('enter a number'))
# if a%2==0:
#     print (a,'is a even number ')
# else:
#     print (a,'is odd number')

# a=int(input('enter a number'))
# b=int(input('enter a number'))
# c=int(input('enter a number'))
# if a>b and a>c:
#     print ('greatest number is',a)
# elif b>a and b>c:
#     print ('greatest number is',b)
# else:
#     print ('greatest number is',c)

# print("finding greatest number with out using and oprator")
# a=int(input('enter the number'))
# b=int(input('enter the number'))
# c=int(input('enter the number'))
# if a==b:
#    print('and b are equel') 
# if a>b:
#     if a>c:
#      print(a,'is the greatest ')
#     else:
#        print(c,'is the greatest')
# else:
#    if b==c:
#       print ('b and c are equal')
#    if b>c:
#       print(b,'is the greatest')
#    else:
#       print (c,'is the geatest')

# print('to find the circumference of the circle')
# r=float(input(" enter the \n radiuse of the circle:"))
# pi=3.14
# radius=2*pi*r
# if r<0:
#  print("invalide input")
# else :
#  print('circumference=',radius)

# print('to find he area of the triangle')
# r=float(input('enter the radius of the circle'))
# pi=3.14
# area=pi*r*r
# if r<=0 :
#     print('invaliede input')
# else:
#     print('area of the circle is :',area)

# print('to convert degree into radian')
# d=float(input('ENTER THE ANGLE (degree)= '))
# pi=3.14
# rad=d*(pi/180)
# if d<=0:
#     print('invalied input')
# else:
#     print('the radian vaue of the degreeis= ',rad)
    
# def calculator():
#     num1=float(input('enter the first number'))
#     op=input('ener the operatopr')
#     num2=float(input('ener the second number'))
#     result=0

#     if op=='+':
#         result=num1+num2
#     elif op=='-':
#         result=num1-num2
#     elif op=='*':
#         result=num1*num2
#     elif op=='/':
#         if num2==0:
#             result="error:divition by zero"
#         else:
#             result=num1/num2
#     else:
#         result="error :invalied operatopr "

#     print (result)
#     return(result)

# calculator()

# a=int(input('enter the mark'))
# if a>=80 and a<=100:
#       print('A')
# elif a>60 and a<80:
#       print('B')
# elif a>40 and a<60:
#       print('C')
# elif a>20 and a<40:
#       print('D')
# elif a>14 and a<20:
#       print('E')
# elif a<40:
#       print ('feiles')
# else:
#       print('invalied input')
# # 

# largest=0
# for num in range(0,101):
#     if num>largest :
#         largest=num
# print (largest,'is the largest')


# i=0
# for i in range(0,101):
#     if i%3==0 and i%5==0:
#         print (i,'fizzbuzz')
#     elif i%3==0:
#         print(i,'fizz')
#     elif i%5==0:
#         print(i,'buzz')
#     elif i%3==0 and i%5==0:
#         print (i,'fizzbuzz')  
# for i in range (1,6):
#     for j in range(i):
#        print('*',end="")
    # print()
# greater=0
# for i in range(0,101):
#     if(i<=(i+1)):
#         greater=i
# print('greatest nomber is',greater)
# n=5
# for i in range(1,n-1):
#     print('*'*i)