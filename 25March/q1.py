'''
Write a program that processes a given string to determine:
1.The first non-repeating character (if present).
2.The most repeated character in the string.
If multiple characters have the same highest frequency, print the first non-repeating
character first, then the most repeated character.
3.
4.If the input string is empty, print "Invalid Input".
If all characters in the string are repeating, print "None" followed by the most repeating
character.
'''
from collections import Counter

s = input().strip()

if not s:
    print("Invalid Input")
else:
    freq = Counter(s)
    first_non_repeating = None

    for char in s:
        if freq[char] == 1:
            first_non_repeating = char
            break

    max_freq = 0
    most_repeated_char = None
    for char in s:
        if freq[char] > max_freq:
            max_freq = freq[char]
            most_repeated_char = char

    if first_non_repeating:
        print(f"non repeating {first_non_repeating}, most repeated {most_repeated_char} -> fre = {max_freq}")
    else:
        print(f"None {most_repeated_char}")
