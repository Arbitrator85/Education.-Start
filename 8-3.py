import math
m = int(input())
n = int(input())
z = []
for i in range(n):
    new_n = int(input())
    if 1 <= m <= 10e6 and 1 <= n <= 100 and 1 <= new_n <= m:
        z.append(new_n)

print(math.ceil(sum(z)/m))