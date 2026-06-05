arr=[1,2,3,4,5,6]
target=6
l=0
r=len(arr)-1
while l<=r:
    sum=arr[l]+arr[r]
    if sum==target:
        print(arr[l],arr[r])
        print("Indexes are",l,r)
        break
    elif sum<target:
        l+=1
    else:
        r-=1