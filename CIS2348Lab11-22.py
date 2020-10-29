words = input().split()
for x in words:
    count = 0
    for i in words:
        if i == x:
            count += 1
    print(x, count)
