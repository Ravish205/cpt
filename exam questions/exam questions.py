def safe_check(t,N,A):
     results=[]
     for i in range(t):
         full_number_string="".join(map(str,A[i]))
         if len(full_number_string)<2:
             if full_number_string=="0":
                 results.append("YES")
             else:
                 results.append("NO")
         else:
             last_two=full_number_string[-2:]
             if last_two in ["00","25","50","75"]:
                 results.append("YES")
             else:
                 results.append("NO")
     return results

if __name__ == "__main__":
     t=int(input())
     A=[]
     N=[]
     for i in range(t):
         N.append(int(input()))
         a=[]
         temp=input().split()
         m=map(int,temp)
         L=list(m)
         A.append(L)
     res=safe_check(t,N,A)
     for r in res:
         print(r)


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


def findTopper(studentTuple):
    # WRITE YOUR LOGIC HERE:
    
    # Initialize variables to keep track of the highest marks and the student's name
    # max_marks = -1
    # topper_name = ""
    
    # # Iterate through each record in the studentTuple
    # # Each record is (ID, Name, Marks)
    # for student in studentTuple:
    #     name = student[1]
    #     marks = student[2]
        
    #     # Check if the current student's marks are greater than the current max
    #     if marks > max_marks:
    #         max_marks = marks
    #         topper_name = name
            
    # return topper_name
    # find the tuple with the maximum value at index 2 (marks)
    topper = max(studentTuple, key=lambda x: x[2])
    # return the name (index 1) of that tuple
    return topper[1]

# Non editable starts here
if __name__ == "__main__":
    n = int(input())
    records = []
    for _ in range(n):
        data = input().split()
        records.append((int(data[0]), data[1], int(data[2])))
    studentTuple = tuple(records)
    print(findTopper(studentTuple))
# Non editable ends here