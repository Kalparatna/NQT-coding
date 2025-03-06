n, k = map(int, input().split())
coins_in_rooms = list(map(int, input().split()))

for i in range(n):
    for j in range(i + 1, n + 1):  
        if sum(coins_in_rooms[i:j]) == k:
            print(i + 1, j)  
            exit()
