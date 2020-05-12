def solve():
    n = int(input())
    arr_a = [int(a) for a in input().split()]
    partial = 0
    maximum1 = -5
    maximum_i = -5
    temp = -5
    max_temp = -5
    results = []

    for i in range(n):
        partial = partial + arr_a[i]
        
        if arr_a[i] > maximum1: 
            maximum1 = arr_a[i]
            maximum_i = i
    
    for i in range(n):
        if i == maximum_i:
            continue
        if arr_a[i] > temp:
            temp = arr_a[i]
            max_temp = i

    for i in range(n):
        if i == maximum_i:
            if partial - arr_a[i] - temp == temp:
                adicionar = i + 1
                results.append(adicionar)
        else:
            if partial - arr_a[i] - maximum1 == maximum1:
                adicionar = i + 1
                results.append(adicionar)

    print(len(results))

    if len(results) == 0:
        return
    
    for i in range(len(results)):
        if i == len(results) - 1: 
            print(results[i])
            return
        else: print(results[i], end=' ')

solve()