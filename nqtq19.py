'''
Write a program to reverse a string without using inbuilt string reverse library functions
'''

# Solution
'''

st = input()
reversed_string = ""

for i in st:
    reversed_string = i + reversed_string

print(reversed_string)

'''

# Or Using stack

st = input()
stack=  list(st)

reversed_string = ""

while stack:
    reversed_string += stack.pop()

print(reversed_string)