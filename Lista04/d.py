minimum = -2000000000
maximum = 2000000000

n = int(input())

while(n > 0):
    n -= 1

    entrada = input().split()

    q = entrada[0]
    num = int(entrada[1])
    result = entrada[2]

    if(q == ">" and result == "Y"):
        minimum = max(minimum, num + 1)
    elif(q == ">" and result == "N"):
        maximum= min(maximum, num)
    elif(q == ">=" and result == "Y"):
        minimum = max(minimum, num)
    elif(q == ">=" and result == "N"):
        maximum= min(maximum, num - 1)
        
    elif(q == "<" and result == "Y"):
        maximum= min(maximum, num - 1)
    elif(q == "<" and result == "N"):
        minimum = max(minimum, num)
    elif(q == "<=" and result == "Y"):
        maximum= min(maximum, num)
    elif(q == "<=" and result == "N"):
        minimum = max(minimum, num + 1)

if (minimum <= maximum):
    print(minimum)
else:
    print("Impossible")