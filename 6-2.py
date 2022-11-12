x = int(input())

if x == 1:
    s = 1
else:
    s = 2
    for i in range(2, int((x/2) + 1)):
        if x % i == 0:
            s += 1

print(s)