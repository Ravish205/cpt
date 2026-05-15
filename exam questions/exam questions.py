# def safe_check(t,N,A):
#      results=[]
#      for i in range(t):
#          full_number_string="".join(map(str,A[i]))
#          if len(full_number_string)<2:
#              if full_number_string=="0":
#                  results.append("YES")
#              else:
#                  results.append("NO")
#          else:
#              last_two=full_number_string[-2:]
#              if last_two in ["00","25","50","75"]:
#                  results.append("YES")
#              else:
#                  results.append("NO")
#      return results

# if __name__ == "__main__":
#      t=int(input())
#      A=[]
#      N=[]
#      for i in range(t):
#          N.append(int(input()))
#          a=[]
#          temp=input().split()
#          m=map(int,temp)
#          L=list(m)
#          A.append(L)
#      res=safe_check(t,N,A)
#      for r in res:
#          print(r)


# def detect_capital_use(word):
#     if word.isupper():
#         return "True"
#     elif word.islower():
#         return "True"
#     elif word.istitle():
#         return "True"
#     else:
#         return "False"

# if __name__ == "__main__":
#     word=input()
#     print(detect_capital_use(word))


# def findTopper(studentTuple):
    # max_marks = -1
    # topper_name = ""
    # for student in studentTuple:
    #     name = student[1]
    #     marks = student[2]
    #     if marks > max_marks:
    #         max_marks = marks
    #         topper_name = name
    # return topper_name
    # topper = max(studentTuple, key=lambda x: x[2])
    # return topper[1]
# if __name__ == "__main__":
#     n = int(input())
#     records = []
#     for _ in range(n):
#         data = input().split()
#         records.append((int(data[0]), data[1], int(data[2])))
#     studentTuple = tuple(records)
#     print(findTopper(studentTuple))


# def power_set(A):
#     N=len(A)
#     if N==0:
#         return 1
#     return 2**(N-1)
# if __name__ == "__main__":
#     N=int(input())
#     A=list(map(int,input().split()))
#     print(power_set(A))