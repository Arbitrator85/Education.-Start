a = int(input())
z = list(map(int,input().split()))
for i in range(1):
    if len(z) == a and 1 <= a <= 100000 and abs(z[i]) <= 2*10e9:
        print(len(set(map(int, z))))
    else:
        print("Error")