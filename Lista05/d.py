entrada = input()

n = int(entrada.split()[0])
k = int(entrada.split()[1])

cc =  n - k

flag = 1

i = 1
while(i <= n - k):
    print(i, end=" ")
    i += 1

i = k
while (i >= 1):
    if (flag == 1):
        if (i == 1):
            print(cc + i)
        else:
            print(cc + i, end=" ")
        cc += i
        flag = 0
    else:
        if (i == 1):
            print(cc - i)
        else:
            print(cc - i, end=" ")
        cc -= i
        flag = 1
    i -= 1