a = int(input())
def fun(a):
    z = list(map(int,input().split()))
    for i in range(len(z)):
        if 1<=a<=100000 and 1<=z[i]<=10e9:
            z.insert(0,z[-1])
            return z[0:a]
            
print(fun(a))