"""method 1"""
# n=[1, 2, 3, 4]
# result=[]
# for i in n:
#     product=1
#     for j in n:
#         if i!=j:
#             product*=j
#     result+=[product]
# print(result)
"""method2"""
# n=[1,2,3,4]
# result=[]
# for i in range(len(n)):
#     product=1
#     for j in range(len(n)):
#         if i!=j:
#             product*=n[j]
#     result.append(product)
# print(result)
"""in a gien lst [1,2,0,4,5,0] all the zeros should be in the last """
l=[1, 2, 0, 4, 5, 0]
result=[x for x in l if x!=0]+[0]*l.count(0)
print(result)

l=[1,0,3,0,4,5]
b=[]
for i in l:
    if i!=0:
        b+=[i]
print(b+[0]*l.count(0))