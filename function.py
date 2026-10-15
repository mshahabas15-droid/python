# DEFOULT ARGUMENT*********

# def greet(name,b='goodmorning'):
#     return(b,name)
# print(greet('shahabas'))
#****************************

# A=greet('niya') 
# print(A)   


#***************************

#KEY WORD ARGUMENT***********
# def great(name,greet="hello"):
#     print(greet,name) 
    

# great(name="sha",greet="hi")

# def add(a,b):
#     print(a)
#     return a+b
# p=add(56,67)
# print(p)

# def add(a,b):
#     print(x)
#     return a+b
# x=10
# p=add(56,67)
# print(x)


# def add(a,b):
#     # print(a)
#     return a-b
# p=add(56,67)
# print(p)

# def add(a,b):
#     # print(a)
#     return a%b
# p=add(56,67)
# print(p)

# def add(a,b):
#     p=a+b
#     return (p)
# print(add(2,5))



#*************************************
# def fact(n):
#     a=1
#     i=1
#     if n<0:
#         print('invalied input')
#     else:
#         for i in range(1,n):
#             a*=i
#         print(a) 
#     return (n)

# print(fact(c))

#******************************************
# inpt1=int(input('enter the value ='))
# inpt2=int(input("enter the value ="))

# def calc(inpt1 ,inpt2=3):
#     a=inpt1+inpt2
#     # print(a)
#     return(a)

# t=calc(inpt1=5,inpt2=2)
# print(t)


#*********************************************
# num1=int(input('enter the first number= '))
# op=input('enter the perator= ')
# num2=int(input ('enter the secound number= '))
  
# def calc(num1,op,num2):
#     if op=="+":
#         a=num1+num2
#         # print(a)
#         return(a)

#     elif op=="-":
#         b=num1-num2
#         # print(b)
#         return(b)

#     elif op=="*":
#         c=num1*num2
#         # print(c)
#         return(c)

#     elif op=="/":
#         d=num1/num2
#         # print(d)
#         return(d)
    
#     elif op=="**" :
#         e=num1**num2
#         # print (e)
#         return(e)

#     # return(a,b,c,d)

# t= calc(num1,op,num2)
# print(t)

#*************************************


# def happy_birthday(name, age):
#     print('happy birthday to',name)
#     print(f'you are {age}yers old !')
#     print('happ ybirth day to',name)
#     print()

# happy_birthday(name='bro',age=23)
# happy_birthday(age='shahabas',name=22)

#******************************************

#whire the function to find the three sides of atriangle is right agle triagle sides?

# a=10
# b=20
# c=15
# def find(side1,side2,side3):
#     sides=[side1,side2,side3]
#     sides.sort(reverse=True)
#     s=sides[1]**2+sides[2]**2
#     if s==sides[0]**2:
#         print('it is the sides of right triangle')
#     else:   
#        print('its not the sides of right angle triangle')

# find(a,b,c)

# find the number is odd or even ?
# def find(a):
#     if a%2==1:
#         return True
#     else:
#         return False

# if (find(23)):
#     print('it is an even number')
# else:
#     print('it is an odd number')

#++++++++++++++++++++++++++++++++++++++++++++++

# def qube(a):
#     return a**3

# print(qube(2))
#****************************
# abcd=[2,4,6,8,9]
# b=[]
# for i in (abcd) :
#     b.append(i*i*i)

# print(b)

#***************************
# x=int(input ('enter the number'))
# cube=int(lambda x:x**3)
# print(cube)