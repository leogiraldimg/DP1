n = int(input())
s = input()

i = 0
answer = "NO"
example = ""
while(i < n):
    if (i == n -1):
        break

    if (s[i] != s[i+1]):
        answer = "YES"
        example = s[i] + s[i+1]
        break

    i += 1

print(answer)
 
if (example != ""):
    print(example)