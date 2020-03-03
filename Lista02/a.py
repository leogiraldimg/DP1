entrada = input()

n1 = int(entrada.split(" ")[0])
n2 = int(entrada.split(" ")[1])
k1 = int(entrada.split(" ")[2])
k2 = int(entrada.split(" ")[3])

while True:
    n1 = n1 - 1
    n2 = n2 - 1

    if (n1 == 0 and n2 >= 0):
        print("Second")
        break
    
    if (n2 == 0 and n1 > 0):
        print("First")
        break