'''
Program to add two fractions and display their sum in reduced form
Public Test cases:

Input: 1 2 3 2

Output: 2 1

Input: 1 3 3 9

Output: 2 3
'''
import math

def add_fractions(num1, den1, num2, den2):
    den_mul = den1 * den2
    n1_d2 = num1 * den2
    n2_d1 = num2 * den1

    nur_add = n1_d2 + n2_d1
    gcd = math.gcd(nur_add, den_mul)

    reduced_nur = nur_add // gcd
    reduced_den = den_mul // gcd

    return reduced_nur, reduced_den

num1, den1, num2, den2 = map(int, input().split())
reduced_nu,reduced_den = add_fractions(num1, den1, num2, den2)
print(reduced_nu,reduced_den)
