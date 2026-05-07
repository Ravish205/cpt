#greatest of two number using operators
a,b=int(input("enter a number:")),int(input("enter another number:"))
greatest=a if a>b else b
print(f"the greatest number is {greatest}")
print(type(greatest))