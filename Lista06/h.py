n = int(input())
arr_a = [int(a) for a in input().split()]
arr_st = []
guardar = [0] * 100007
result = 1

i = 0
while(i < n):
    
    j = 2
    while(j * j <= arr_a[i]):
        j += 1

        if (arr_a[i] % j == 0):
            arr_st.append(j)
            arr_st.append(arr_a[i] // i)
    
    if (len(arr_st) == 0 and arr_a[i] != 1):
        arr_st.append(arr_a[i])
    
    bmx = 0

    for st in arr_st:
        bmx = max(bmx, guardar[st])

    for st in arr_st:
        guardar[st] = bmx + 1
    
    result = max(result, bmx)

    i += 1

print(result)