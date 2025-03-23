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
