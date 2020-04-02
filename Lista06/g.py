n = int(input())
arr_p = [int(p) for p in input().split()]

for i in range(0, n):
    h = [0] * n

    j = i
    while(h[j] < 2):
        h[j] += 1
        j = arr_p[j] - 1
    
    print(j + 1)