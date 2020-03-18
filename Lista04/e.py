entrada = input().split()

a = int(entrada[0])
b = int(entrada[1])

if (a == b):
    print("infinity")
else:
    a -= b
    result = 0

    i = 1
    while(i * i <= a):
        if (a % i == 0):
            if (i > b):
                result += 1
            if (a // i != i and (a // i) > b):
                result += 1
        i += 1
    
    print(result)