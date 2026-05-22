"""input with 15 elements caculate sum of 3 elements like '1+2+3 next 2+3+4' etc which contains maximum number and give the index value of maximum number"""

arr=[1,2,3,4,5,6,7,8,9,10]
max_sum=0
max_index=0
for i in range(len(arr)-2):
    total=arr[i]+arr[i+1]+arr[i+2]
    print(f"{arr[i]}+{arr[i+1]}+{arr[i+2]}={total}")
    if total>max_sum:
        max_sum=total
        max_index=i
print("\nMaximum Sum:",max_sum)
print("Index:",max_index)