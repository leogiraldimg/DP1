config = input()
config_splitted = config.split(" ")
num_segments = int(config_splitted[0])
upper_bound = int(config_splitted[1])
axis = [0] * 110

i = 0
for i in range(num_segments):
    segment = input()
    l = int(segment.split(" ")[0])
    r = int(segment.split(" ")[1])

    j = l
    while (j <= r):
        axis[j] = 1
        j = j + 1

num_not_in_segment = 0
not_in_segment = []

i = 1
while (i <= upper_bound):
    if axis[i] == 0:
        num_not_in_segment = num_not_in_segment + 1
        not_in_segment.append(i)
    i = i + 1
    
print(str(num_not_in_segment))

if num_not_in_segment > 0:
    num = 0
    for num in range(len(not_in_segment)):
        if (num == len(not_in_segment) - 1):
            print(str(not_in_segment[num]))
        else:
            print(str(not_in_segment[num]), end = " ")