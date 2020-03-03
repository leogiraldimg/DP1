def existsValueInList(arr, value):
    exist = False
    for val in arr:
        if val == value:
            exist = True
    return exist


n = int(input())
arr_divisors_str = input().split(" ")
arr_divisors_int = [int(i) for i in arr_divisors_str]
tmp_max = 0
arr_set = []

i = 0
while (i < n):
    arr_set.append(arr_divisors_int[i])
    tmp_max = max(tmp_max, arr_divisors_int[i])
    i += 1

i = 1
while (i <= tmp_max):
    if (tmp_max % i == 0):
        if (existsValueInList(arr_set, i)):
            arr_set.remove(i)
    i += 1
        

arr_set.sort()
print(str(tmp_max) + " " + str(arr_set[len(arr_set) - 1]))