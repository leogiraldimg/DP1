n = int(input())
a = input().split()
a = [int(i) for i in a]
m = int(input())
q = input().split()
q = [int(i) for i in q]

result = 0

i = 0   
while i < n:
    result += a[i]
    i += 1

a.sort(reverse=True)

for i in range(m):
    print(result - a[q[i] - 1])