s = input()
c = 0

for i in range(0, len(s)):
    if ((ord(s[i]) - ord('0')) % 4 == 0):
        c += 1

for i in range(0, len(s) - 1):
    if(((ord(s[i]) - ord('0')) * 10 + (ord(s[i + 1]) - ord('0'))) % 4 == 0):
        c += i + 1

print(c)