n = int(input())
result = []

for i in range(n):
    entrada = int(input())

    if entrada % 4 == 0:
        result.append(entrada // 4)
    
    elif entrada % 4 == 1:
        if entrada < 9:
            result.append(-1)
        
        else:
            result.append(((entrada - 9) // 4) + 1)
        
    elif entrada % 4 == 2:
        if entrada < 6:
            result.append(-1)
        
        else:
            result.append(((entrada - 6) // 4) + 1)
        
    else:
        if entrada <= 11:
            result.append(-1)
        
        else:
            result.append(((entrada - 9) // 4) + 1)

for r in result:
    print(r)
