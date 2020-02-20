num_queries = int(input())
arr_queries = []

for x in range(num_queries):
    arr_queries.append(input())

for query in arr_queries:
    query_splited = query.split(" ")
    l1 = int(query_splited[0])
    r1 = int(query_splited[1])
    l2 = int(query_splited[2])
    r2 = int(query_splited[3])

    minl = min(l1, l2)

    if minl == l1:
        x = l2
        while (x <= r2):
            x = x + 1
            if (x != minl):
                print(str(minl) + " " + str(x))
                break
    else:
        y = r1
        while (y >= l1):
            y = y - 1
            if (y != minl):
                print(str(y) + " " + str(minl))
                break