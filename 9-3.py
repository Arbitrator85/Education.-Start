a = list(map(int, input().split()))
newset = set()
for i in a:
    if i in newset:
        print('YES')
    else: 
        print('NO')
    newset = list(set(newset) | {i})