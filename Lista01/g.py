import math

config = input()
config_splitted = config.split(" ")
max_value_coins = int(config_splitted[0])
total_value = int(config_splitted[1])

cnt = 0
i = max_value_coins
k = 0
while (i > 0):
    k = total_value / i
    cnt = cnt + k
    total_value = total_value - (k * i)
    i = i - 1

print(math.ceil(cnt))