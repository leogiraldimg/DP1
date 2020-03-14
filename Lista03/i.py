n = int(input())

if (n%2 == 0):
    if (n%4 == 0):
        print(0)
        print(int((n // 4) * 2), end=" ")

        i = 1
        while (i <= n//4):
            print(str(i) + " " + str(n - i + 1), end=" ")
            i += 1
        print()
    else:
        print(1)
        print(int(n // 4 * 2 + 1), end=" ")

        i = 1
        while(i <= n/4):
            print(str(i) + " " + str(n - i + 1), end=" ")
            i += 1

        print(int(n//2))

else:
    if ((n + 1)%4 == 0):
        print(0)
        print(int((n + 1) // 4 * 2), end=" ")
    
        i = 1
        while(i <= (n + 1) // 4):
            if ((n + 1) / 4 == i):
                print(str(i) + " " + str(int((n + 1) // 2)), end=" ")
            else:
                print(str(i) + " " + str(n - i + 1), end=" ")
            i += 1
        
        print()
    else:
        print(1)
        print(str(int((n + 1) // 4 * 2)), end=" ")

        i = 1
        while(i <= ((n+1)//4)):
            if ((n+1)//4 == i):
                print(str(int((n + 1) // 2)) + " " + str(n - i + 1), end=" ")
            else:
                print(str(i) + " " + str(n - i + 1), end=" ")
            i += 1
        print()
