entrada = int(input())

def solve():
    print(entrada)
    arr_a = [0] * entrada
    contador = 1
    
    i = 0
    while i < len(arr_a):
        arr_a[i] = contador
        contador += 1
        i += 2
    
    i = 1
    while i < len(arr_a):
        arr_a[i] = contador
        contador += 1
        i += 2
    
    for a in arr_a:
        print(a, end=' ')
    print()

if entrada == 1 or entrada == 2:
    print(1)
    print(1)
elif entrada == 3:
    print(2)
    print('1 3')
elif entrada == 4:
    print(4)
    print('2 4 1 3')
else:
    solve()