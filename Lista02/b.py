n = int(input())

entrada_a = input()
arr_a = entrada_a.split(" ")

arr_a_int = [int(i) for i in arr_a] 

sum_arr_a = sum(arr_a_int)

result = 0
if sum_arr_a % 2 == 0:
    for bag in arr_a_int:
        if (bag % 2 == 0):
            result = result + 1
else:
    for bag in arr_a_int:
        if (bag % 2 != 0):
            result = result + 1

print(result)