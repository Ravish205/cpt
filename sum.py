arr=[-2,1,-3,4,-1,2,1,-5,4]
cs=0
ms=arr[0]
for i in arr:
    cs+=i
    if(cs>ms):
        ms=cs
    if(cs<0):
        cs=0
print(ms)