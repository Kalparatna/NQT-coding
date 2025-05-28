'''
Q1)Write a program in to check whether two given strings are anagrams of each other or not.
Two strings are said to be anagrams if they contain the same characters in the same frequency, but possibly in a different order.

Input:
Two strings, str1 and str2.
Output:
Print "Anagrams" if the two strings are anagrams.
Print "Not Anagrams" otherwise.

Example:
Input:
str1 = "listen"
str2 = "silent"

Output: 
Anagrams
'''


def isAnagram(str1, str2):
    if len(str1)!=len(str2):
        return False
    
    fre1 = {}
    fre2 = {}

    for i in str1:
        fre1[i] = fre1.get(i, 0)+1

    for i in str2:
        fre2[i] = fre2.get(i, 0)+1

    return fre1 == fre2

str1 = input()
str2 = input()
if isAnagram(str1, str2):
    print("Anagram")
else:
    print("Not Anagram")

# Or 

str1 = input()
str2 = input()

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")

