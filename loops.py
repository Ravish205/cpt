# count=0
# for n in range(18,51):
#     if n%7==0:
#          print(n)
#          count+=1
#     if count==2:
#         break
# for i in range(1,21):
#     if i%4==0:
#         continue
#     print(i)
"""prints 1 to 10 numbers using while loop"""
# n=1
# while n<11:
#     print(n)
#     n+=1
"""suqare of 1 to 5 numbers"""
# for i in range(1,6):
#     exp=i**2
#     print(exp)
"""skips number 3 and print remaining numbers range 1 to 5"""
# for i in range(1,6):
#     if i==3:
#         continue
#     print(i)
"""multiplication table"""
# n=int(input())
# for i in range(1,11):
#      print(n,"X",i,"=",n*i)
"""uses break statment to exit loop sfter printing 1 to 10 numbers when the number 5 encountered"""
# for i in range(1,11):
#     print(i)
#     if i==5:
#         break
"""Factorial"""
# n=int(input())
# result=1
# for i in range(1,n+1):
#     result*=i
# print(f"factorial of {n}! is {result}")
"""reverse of a number 123 in python"""
# num = int(input("Enter a number:"))
# reversed_num = 0
# while num > 0:
#     digit = num % 10 
#     reversed_num = reversed_num * 10 + digit  
#     num //= 10         
# print(reversed_num)
"""sum of first five natural numbers"""
# n=0
# for i in range(1, 6):
#     n+=i
# print(n)
"""sum of digits in a number"""
# num=int(input("Enter a number:"))
# sum=0
# while num>0:
#     sum+=num % 10
#     num=num // 10         
# print("Sum of digits:",sum)
"""palindrome"""
# num=int(input("Enter a number:"))
# original=num
# reversed=0
# while num>0:
#     digit=num % 10
#     reversed=(reversed*10)+digit
#     num=num//10
# if original==reversed:
#     print(f"{original} is a palindrome")
# else:
#     print(f"{original} is not a palindrome")
"""prime number"""
n = int(input("Enter a number: "))
if n>1:
    for i in range(2,n):
        if (n%i)==0:
            print(n,"is not a prime number.")
            break
    else:
         print(n,"is a prime number.")
elif n == 1:
    print("1 is neither prime nor composite.")
else:
    print(n,"is not a prime number.")