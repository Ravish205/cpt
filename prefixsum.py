arr=[2,6,9,12,11,3]
prefix=[0]*len(arr)
prefix[0]=arr[0]
for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]
l=1
r=4
if l==0:
    ans=prefix[r]
else:
    ans=prefix[r]-prefix[l-1]
print(ans)