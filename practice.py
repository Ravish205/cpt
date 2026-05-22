# """prime number"""
# n = int(input("Enter a number: "))
# if n>1:
#     for i in range(2,n):
#         if (n%i)==0:
#             print(n,"is not a prime number.")
#             break
#     else:
#          print(n,"is a prime number.")
# elif n == 1:
#     print("1 is neither prime nor composite.")
# else:
#     print(n,"is not a prime number.")


# """prime numbers in a range"""
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# print(f"Prime numbers between {a} to {b} are:")
# for n in range(a,b+1):
#     if n > 1:
#         for i in range(2,n):
#             if (n%i)==0:
#                 break
#         else:
#             print(n,end=" ")
# print()

# start=int(input("Enter the start of the range: "))
# end=int(input("Enter the end of the range: "))
# opr=input("Enter the operator: ")
# 
# match opr:
#     case "+":
#         print(start+end)
#     case "-":
#         print(start-end)
#     case "*":
#         print(start*end)
#     case "/":
#         print(start/end)
#     case "%":
#         print(start%end)


"""Sum of even numbers in a range using for loop"""
# start=int(input("Enter the start: "))
# end=int(input("Enter the end: "))
# even_sum=0
# for n in range(start,end+1):
#     if n%2==0:
#         even_sum+=n
# print(f"The sum of even numbers between{start}and{end}is:{even_sum}")

"""multiplication table using for loop"""
# start=int(input("Enter the number: "))
# for i in range(1,11):
#     print(start,"*",i,"=",start*i)


"""factor of a number using for loop"""
# start=int(input("Enter the number: "))
# for i in range(1,start+1):
#     if start%i==0:
#         print(i,end=" ")


"""Fibonacci series"""
# n=int(input("Enter the number: "))
# a,b=0,1
# for i in range(n+1):
#     print(a,end=" ")
#     a,b=b,a+b
# print()
# n = int(input("Enter the number of terms: "))
# a,b=0,1
# for i in range(n+1):
#     print(a,end=" ")
#     temp = a + b
#     a = b
#     b = temp
# print()

"""finding maximum element in a array without max()function using for loop """
arr=[1,50,60,80,2,100,2,4,200,3456]
max=0
for i in arr:
    if i>max:
        max=i
print("The maximum element is:",max)