'''
MS Excel columns have a pattern like A, B, C, ..., Z, AA, AB, AC, ...., AZ, BA, BB, ZZ, AAA, AAB ..... etc. In other words, column 1 is named as "A", column 2 as "B", column 27 as "AA".

Given a column number, find its corresponding Excel column name. The following are more examples.


Input

26
51
52
80
676
702
705


Output
Z
AY
AZ
CB
YZ
ZZ
AAC
'''

num = int(input())
result =""
while num>0:
    num -= 1  # 0- based indexing
    result  = chr(num % 26 + ord('A')) + result
    num //= 26

print(result)

