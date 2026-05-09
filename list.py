"""PROBLEMS BASED ON LISTS"""

"""sorting"""
# a=input().split()
# b=input().split()
# c=a+b
# c=[int(i) for i in c]
# c.sort()
# print(c)
"""separation by length"""
# l=input().split()
# l.sort(key=len)
# print(l)
"""removing repeated values from a list"""
# a=[5,9,2,9,3,6,2]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
"""odd number of time repeated in a list"""
# a=input().split()
# b=[]
# for i in a:
#    if a.count(i)%2!=0 and i not in b:
#         b.append(i)
# print(b)
"""swapping of first and last elements"""
# a=input().split()
# a[0],a[-1]=a[-1],a[0]
# print(a)
"""sorting using map function"""
# data=input("Enter the data:")
# a=list(map(int, data.split()))
# print(a)
# a.sort()
# print(a)
"""read a list and print sum of three minimum elements in a list"""
# l=[4,2,3,1,5]
# l.sort()
# print(l)
# b=l[0]+l[1]+l[2]
# print(b)
"""segregate the given list as even elements first in descending and then odd elements in ascending order"""
# l=list(map(int,input().split()))
# even=sorted([x for x in l if x % 2 == 0], reverse=True)
# print(even)
# odd=sorted([x for x in l if x %2!=0])
# print(odd)
# result=even+odd
# print(result)
# """l=list(map(int,input().split()))
# a=[]
# b=[]
# for i in l:
#     if i%2==0:
#         a.append(i)
#         a.sort()
#         a.reverse()
#     else:
#         b.append(i)
#         b.sort()
# print(a+b)"""
"""segregate the given list as even elements first in descending and then odd elements in ascending order using extend and insert"""
# a=list(map(int,input().split()))
# b=[]
# for i in a:
#     if i%2==0:
#         b.insert(0,i)
#     else:
#         b.append(i)
# print(b)