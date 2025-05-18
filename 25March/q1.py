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

def process(s):
    if not s:
        return "Invalid Input"

    # Step 1: Build the frequency dictionary
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Step 2: Find the first non-repeating character
    first_non_repeating = None
    for char in s:
        if frequency[char] == 1:
            first_non_repeating = char
            break

    # Step 3: Find the highest frequency
    max_freq = max(frequency.values())

    # Step 4: Get all characters with max frequency
    most_repeated_chars = [char for char in frequency if frequency[char] == max_freq]

    # Step 5: Among them, get the one that appears first in the string
    most_repeated_char = None
    for char in s:
        if char in most_repeated_chars:
            most_repeated_char = char
            break

    # Step 6: Return results
    if first_non_repeating:
        return f"{first_non_repeating} {most_repeated_char}"
    else:
        return f"None {most_repeated_char}"


s = input("Enter a string: ")
print(process(s))


    



























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
