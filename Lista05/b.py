t = int(input())
tt = t

arr_n = []
arr_s = []

i = 0
while(i < t):    
    arr_n.append(int(input()))
    arr_s.append(input())

    i += 1

k = 0
while(k < tt):
    flag = True

    i = 0
    while (2 * i < arr_n[k]):
        if (ord(arr_s[k][i]) == ord(arr_s[k][arr_n[k] - 1 - i]) or (ord(arr_s[k][i]) - ord(arr_s[k][arr_n[k] - 1 - i]) == 2) or (ord(arr_s[k][arr_n[k] - 1 - i]) - ord(arr_s[k][i]) == 2)):
            i += 1
            continue
        flag = False
        i += 1
    
    k += 1
    
    print("YES" if flag == True else "NO")
    