entrada1 = input()
n = int(entrada1.split()[0])
k = int(entrada1.split()[1])

arr_a = []
entrada2 = input().split()
i = 0
while(i < len(entrada2)):
    arr_a.append(int(entrada2[i]))
    i += 1

if (n == 1):
    print(arr_a[0])

    i = 0
    while(i < k - 1):
        print(0)
        i += 1
    
    exit()

arr_a.sort()

sas = 0
ytpbr = 0

i = 0
while(i < n - 1):
    if (ytpbr == 0 and arr_a[i] != 0):
        print(arr_a[i])
        ytpbr += 1

        if (ytpbr == k):
            break
    
    if (ytpbr > 0):
        if (arr_a[i + 1] > arr_a[i]):
            print(abs(arr_a[i+1] - arr_a[i]))
            sas += 1
    
    if ((sas + ytpbr) == k):
        break

    i+= 1

i = 0
while(i < (k - (sas + ytpbr))):
    print(0)
    i += 1