n = int(input())
entrada_a = input().split()
arr_a = [int(a) for a in entrada_a]

aa = [0] * 100007
dpto = [0] * 100007

for i in range(0, n):
    aa[arr_a[i]] += 1

dpto[0] = 0
dpto[1] = aa[1]

i = 2
while(i <= 100000):
    dpto[i] = max(dpto[i - 1], (dpto[i - 2] + i*aa[i]))
    i += 1 

print(dpto[100000])