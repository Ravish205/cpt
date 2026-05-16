# s=input()
# v=0
# c=0
# for i in s:
#     if i in "aeiouAEIOU":
#         v+=1
#     elif i!="aeiouAEIOU":
#         c+=1
# print("vowels:",v)
# print("consonants:",c)

# s=input()
# a=0
# b=0
# for i in s:
#     if i.isdigit():
#         a+=1
#     elif i.isalpha():
#         b+=1
# print("digits:",a)
# print("alpha:",b)

# s=input("enter the string:")
# print(s.replace(" ","-"))
# result = ""
# for char in s:
#     if char == " ":
#         result += "-"
#     else:
#         result += char
# print(result)

"""length of last word in the given string"""
# s = input("enter the string: ")
# word = s.split()[-1]
# print(len(word))
# def length(s):
#     count=0
#     s=s.strip()
#     for i in range(len(s)-1,-1,-1):
#         if s[i]!=" ":
#             count+=1
#         else:
#             break
#     return count
# print(length(input("enter the string: ")))


"""reverse of a string using slicing and using 2 pointer approch using while loop"""
# s=list(input("enter the string: "))
# #using slicing
# x=s[::-1]
# print("".join(x))
#using 2 pointer approch using while loop
# i = 0
# j = len(s) - 1
# while i < j:
#     s[i],s[j]=s[j],s[i]
#     i += 1
#     j -= 1
# print("".join(s))
"""if input is p&abc@#kj and output should be j&kcb@#ap (reversing letters but keeping special characters in place)"""
# s = list(input("enter the string: "))
# i = 0
# j = len(s) - 1
# while i < j:
#     if not s[i].isalnum():
#         i += 1
#     elif not s[j].isalnum():
#         j -= 1
#     else:
#         s[i], s[j] = s[j], s[i]
#         i += 1
#         j -= 1
# print("".join(s))

"""anagram"""
# s = input("enter first string: ")
# t = input("enter second string: ")
# is_anagram = True
# if len(s) != len(t):
#     is_anagram = False
# else:
#     counter = {}
#     for char in s:
#         counter[char] = counter.get(char, 0) + 1

#     for char in t:
#         if char not in counter or counter[char] == 0:
#             is_anagram = False
#             break
#         counter[char] -= 1
# print(is_anagram)
"""pangram"""
sentence = input("enter the string: ")
l = set()
for char in sentence:
    if char.isalpha():
        l.add(char.lower())
result = len(l) == 26
print(result)