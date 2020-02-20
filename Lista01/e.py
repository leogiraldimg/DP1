# quando alterações em x e y, consecutivamente são inversamente proporcionais
# aumenta x (mantém y) aumenta y (mantém x)
# diminui y (mantém x) aumenta x (mantém y)

num_coord = int(input())
num_dangerous_turns = 0

x = []
y = []
i = 0
for i in range(num_coord + 1):
    coord = input()
    x.append(int(coord.split(" ")[0]))
    y.append(int(coord.split(" ")[1]))

i = 1
for i in range(num_coord):
    if (x[i-1] == x[i]):
        if (y[i] > y[i-1]):
            if (x[i+1] < x[i]):
                num_dangerous_turns = num_dangerous_turns + 1
        else:
            if (x[i+1] > x[i]):
                num_dangerous_turns = num_dangerous_turns + 1
    else:
        if (x[i-1] < x[i]):
            if(y[i+1] > y[i]):
                num_dangerous_turns = num_dangerous_turns + 1 
        else:
            if(y[i+1] < y[i]):
                num_dangerous_turns = num_dangerous_turns + 1

print(num_dangerous_turns)