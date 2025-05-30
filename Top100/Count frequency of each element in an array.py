arr = list(map(int, input().split()))

fre = {}

for i in arr:
    fre[i] = fre.get(i, 0) + 1

for key, value in fre.items():
    print(f"{key}: {value} ")
