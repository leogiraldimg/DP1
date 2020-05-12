def solve():
    n = int(input())
    arr_1 = []
    arr_2 = []

    for i in range(n):
        entrada = input().split()
        arr_1.append(int(entrada[0]))
        arr_2.append(int(entrada[1]))

    arr_a = [0] * 5000010
    
    i = 2
    while i < 5000010:
        i += 1
        if arr_a[i] == 0:
            j = i
            while j < 5000010:
                index = j // i
                arr_a[j] = arr_a[index] + 1
                j += i

    i = 2
    while i < len(arr_a):
        i += 1
        arr_a[i] = arr_a[i] + arr_a[i - 1]
    
    for i in range(len(arr_1)):
        result = arr_a[arr_1[i]] - arr_a[arr_2[i]]
        print(result)

solve()