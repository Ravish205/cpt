"""*
   **
   ***"""
# for i in range(1, 4):
#      print('*' * i)
"""1
   1 2
   1 2 3"""
# for i in range(1, 4):
#      for j in range(1, i + 1):
#          print(j, end=" ")
#      print()
"""reverse triangle """
# n=5
# for i in range(n,0,-1):
#      for j in range(i):
#           print("*",end=" ")
#      print()
"""pyramid"""
# n=5
# for i in range(n):
#      print(" "*(n-i-1)+"* "*(i+1))
"""reverse pyramid"""
# n=4
# for i in range(n,0,-1):
#      print(" "*(n-i)+"* "*i)
"""diamond"""
# n=5
# for i in range(n):
#      print(" "*(n-i-1)+"* "*(i+1))
# for i in range(n-1,0,-1):
#      print(" "*(n-i)+"* "*i)
"""floyds triangle"""
# n=5
# num=1
# for i in range(n):
#      for j in range(i+1):
#           print(num,end=" ")
#           num+=1
#      print()
"""binary triangle"""
# n=5
# for i in range(n):
#      for j in range(i+1):
#           print(j%2,end=" ")
#      print()
"""number triangle"""
n=5
for i in range(n):
   for j in range(n):
      if i==0 or i==n-1 or j==0 or j==n-1:
         print("*",end=" ")
      else:
         print(" ",end=" ")
   print()
   