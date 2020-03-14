t = int(input())

arr_n = []
for i in range(0, t):
    arr_n.append(int(input()))

i = 0
while (i < t):
    example = 1
    result_2 = 0
    result = arr_n[i] * (arr_n[i] + 1) // 2

    while (example <= arr_n[i]):
        result_2 += example
        example = example * 2
    
    print(int(result - result_2 * 2))
    i += 1