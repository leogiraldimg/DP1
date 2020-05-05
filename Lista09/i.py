def resolver():
    entrada = input().split()

    n = int(entrada[0])
    m = int(entrada[1])

    arr_x = [int(x) for x in input().split()]

    a = [0] * 1000001

    for i in range(n):
        x = arr_x[i]
        if x == m:
            a[m] += 1
        else:
            if a[x] >= a[m]:
                a[x] += 1

    i = 1
    while i <= 1 * pow(10, 6):
        if a[i] >= a[m] and i != m:
            print(i)
            return
        i += 1

    print(-1)
    return

resolver()