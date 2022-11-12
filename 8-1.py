a = int(input())
z = []
for i in range(a):
    new_a = int(input())
    if new_a >= 1 and new_a <= 10000 and abs(new_a) <= 10e5:
        z.append(new_a)
    else:
        print("Error")

print(list(reversed(z)))