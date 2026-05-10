"""HOLLOW PATTERNS USING PYTHON"""

"""HOLLOW SQUARE"""
# n=5
# for i in range(n):
#    for j in range(n):
#       if i==0 or i==n-1 or j==0 or j==n-1:
#          print("*",end=" ")
#       else:
#          print(" ",end=" ")
#    print()
"""Hollow right angle triangle"""
# n=5
# for i in range(1,n+1):
#    for j in range(1,i+1):
#       if i==n or j==1 or j==i:
#          print("*",end=" ")
#       else:
#          print(" ",end=" ")
#    print()
"""Hollow inverted right angle triangle"""
# n=5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#        if i==n or j==1 or j==i:
#           print("*",end=" ")
#        else:
#           print(" ",end=" ")
#     print()
"""HOLLOW DIAMOND PATTERN"""
# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(1,2*i):
#         if j==1 or j==2*i-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(1,2*i):
#         if j==1 or j==2*i-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
"""HOLLOW NUMBER SQUARE"""
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#             print(j,end=" ")
#         else:
#             print(" ",end=" ")
#     print()
"""HOLLOW HOURGLASS PATTERN"""
# row=5
# for i in range(row,0,-1):
#     for j in range(row-i):
#         print(" ",end=" ")
#     for j in range(1,2*i):
#         if i==1 or i==row or j==1 or j==2*i-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# for i in range(2,row+1):
#     for j in range(row-i):
#         print(" ",end=" ")
#     for j in range(1,2*i):
#         if i==1 or i==row or j==1 or j==2*i-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()    
"""HOLLOW ALPHABET PATTERN"""
# n=5
# start=ord('A')
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print(chr(start+j),end=" ")
#         else:
#             print(" ",end=" ")
#     print()
"""HOLLOW BUTTERFLY PATTERN"""
# n=5
# for i in range(1, n+1):
#      for j in range(1, i+1):
#          if j==1 or j==i:
#              print("*", end=" ")
#          else:
#              print(" ", end=" ")
#      for j in range(2*(n-i)):
#          print(" ", end=" ")
#      for j in range(1, i+1):
#          if j==1 or j==i:
#              print("*", end=" ")
#          else:
#              print(" ", end=" ")
#      print()
# for i in range(n, 0, -1):
#      for j in range(1, i+1):
#          if j==1 or j==i:
#              print("*", end=" ")
#          else:
#              print(" ", end=" ")
#      for j in range(2*(n-i)):
#          print(" ", end=" ")
#      for j in range(1, i+1):
#          if j==1 or j==i:
#              print("*", end=" ")
#          else:
#              print(" ", end=" ")
#      print()