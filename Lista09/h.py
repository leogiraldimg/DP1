def ajustar(h, w, x, y):
    return (x <= h and y <= w) or (y <= h and x <= w)

n = int(input())
arr_r = []

mx = -1
my = -1

for i in range(n):
    entrada = input().split()

    t = entrada[0]
    x = int(entrada[1])
    y = int(entrada[2])

    if t == '+':
        if x < y:
            temp = x
            x = y
            y = temp
        mx = max(mx, x)
        my = max(my, y)
    elif t == '?':
        result = 'YES' if ajustar(x, y, mx, my) else 'NO'
        arr_r.append(result)

for r in arr_r:
    print(r)