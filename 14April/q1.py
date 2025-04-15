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
str1, str2 = map(str, input().split())

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")