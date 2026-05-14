# def safe_check(t,N,A):
#     results=[]
#     for i in range(t):
#         full_number_string="".join(map(str,A[i]))
#         if len(full_number_string)<2:
#             if full_number_string=="0":
#                 results.append("YES")
#             else:
#                 results.append("NO")
#         else:
#             last_two=full_number_string[-2:]
#             if last_two in ["00","25","50","75"]:
#                 results.append("YES")
#             else:
#                 results.append("NO")
#     return results

# if __name__ == "__main__":
#     t=int(input())
#     A=[]
#     N=[]
#     for i in range(t):
#         N.append(int(input()))
#         a=[]
#         temp=input().split()
#         m=map(int,temp)
#         L=list(m)
#         A.append(L)
#     res=safe_check(t,N,A)
#     for r in res:
#         print(r)


def detect_capital_use(word):
    if word.isupper():
        return "True"
    elif word.islower():
        return "True"
    elif word.istitle():
        return "True"
    else:
        return "False"

if __name__ == "__main__":
    word=input()
    print(detect_capital_use(word))