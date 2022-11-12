def fac(n):

    if n == 0:

        return 1

    return fac(n-1) * n

   

z = []

a = int(input())

for i in range(a, 0, -1):

    z.append(fac(i))

print(z)