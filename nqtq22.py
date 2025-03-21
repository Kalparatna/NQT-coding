'''
Given a string S that represents column title of an Excel sheet, find the number that represents that column.

In excel A column is number 1, AA is 27 and so on.

Input:

A single 

line of input containing string S.

Output:

Print the column number


Constraints: 1 ≤ |S| <=7

Example:

Input

A

AA

Output

1

27
'''
st = input()
result = 0

for i in st:
    result = result * 26 + (ord(i) - ord('A') + 1)

print(result)
