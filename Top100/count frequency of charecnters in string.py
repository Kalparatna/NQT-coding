s = input("Enter a string: ")

fre = {}

for char in s:
    fre[char] = fre.get(char, 0) + 1

for key, value in fre.items():
    print(f"{key}: {value}")

print(fre.items())