"""54321"""
# def fun(num):
#     if num==0:
#         return 0
#     else:
#         print(num)
#         fun(num-1)
# fun(5)

"""12345"""
# def fun(num):
#     if num==0:
#         return 0
#     else:
#         fun(num-1)
#         print(num)
# fun(5)

"""5 3 1 3 5"""
# def fun(n):
#     if n==0:
#         return 0
#     if n%2!=0:
#         print(n)
#     fun(n-1)
#     if n%2!=0 and n!=1:
#         print(n)
# fun(5)

"""531"""
# def fun(n):
#     if n == 0:
#         return 0
#     fun(n-1)
#     if n % 2 != 0:
#         print(n)
# fun(5)

"""135"""
# def fun(n):
#     if n == 0:
#         return 0
#     if n % 2 != 0:
#         print(n)
#     fun(n-1)
# fun(5)

"""problems on functions"""
"""1.factorial of n given number using recruction method"""
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# n=int(input("enter the number:"))
# print(fact(n))
"""
2.sum of first n natural numbers using recruction method
"""
# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return n+sum(n-1)
# n=int(input("enter the number:"))
# print(sum(n))


"""
3. fibonacci series using recruction method
"""
# def fib(n):
#      if n<=1:
#          return n
#      else:
#          return fib(n-1)+fib(n-2)
# n=int(input("enter the number:"))
# print(fib(n))
# print([fib(i) for i in range(n)])


"""
4.sum of digits using recrution method
if the input is 123 then sum of digits is 1+2+3=6
"""
# def sum(n):
#      if n==0:
#          return 0
#      else:
#          return n%10+sum(n//10)
# n=int(input("enter the number:"))
# print(sum(n))


"""
5.power of a number using recruction method
"""
# def power(n,e):
#     if e==0:
#         return 1
#     return n*power(n,e-1)
# n=int(input("enter the base:"))
# e=int(input("enter the exponent:"))
# print(power(n,e))


"""
6.the given number is a perfect square or not using recruction method
"""
# def perfect_square(n, i=0):
#      if n < 0:
#          return False
#      if i * i == n:
#          return True
#      if i * i > n:
#          return False
#      return perfect_square(n, i + 1)
# n = int(input("enter the number:"))
# if perfect_square(n):
#      print(f"given number {n} is a perfect square")
# else:
#      print(f"given number {n} is not a perfect square")


"""
7.reduce to the no 1 
if n=16 
16/2=8
8/2=4
4/2=2
2/2=1
n=15 it should get less number of steps
15-1=14
14/2=7
7-1=6
6/2=3
3-1=2
2/2=1
using recrution method
"""
def reduce_to_one(n):
    if n==1:
        return 0
    if n%2==0:
        return 1+reduce_to_one(n//2)
    else:
        return 1+reduce_to_one(n-1)
n=int(input("enter the number:"))
print(reduce_to_one(n))
