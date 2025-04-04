'''

find gcd of number and LCM
'''
#GCD
from math import gcd
n1, n2 = map(int, input().split())
gcd_num = gcd(n1, n2)

print(gcd_num)

#for LCM
lcm_num =  (n1 * n1) // gcd_num
print(lcm_num)



#or

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)  

# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Finding GCD and LCM
gcd_result = gcd(num1, num2)
lcm_result = lcm(num1, num2)

print(f"GCD of {num1} and {num2} is {gcd_result}")
print(f"LCM of {num1} and {num2} is {lcm_result}")

