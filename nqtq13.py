'''
Write a program to check whether a year is a leap year or not?

Public Test Cases:

Input: 2016

Output: Leap Year

Input: 2019

Output: Not a Leap Year
'''

year = int(input())

if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
    print("Leap Year")
else:
    print("Not")