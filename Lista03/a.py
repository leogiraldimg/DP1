n = int(input())
d = input().split()
d = [int(i) for i in d]
st = input()
s = int(st.split()[0])
t = int(st.split()[1])

if (s == t):
    print(0)    
else:
    d.append(0)
    d.insert(0, 0)

    for i in range(2, n + 2):
        d[i] += d[i-1]

    if (s > t):
        temp = t
        t = s
        s = temp

    result = d[t-1] - d[s-1]
    result = min(result, (d[n+1] - result))
    
    print(result)

