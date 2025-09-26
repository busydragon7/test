target = int(input())
a = []
n = int(input())
for k in range(n):
    g=int(input(str(k+1)+": "))
    a.append(g)
p=[]
for k in range(n):
    for j in range(k+1, n):
        if a[k]^a[j]==target:
            p.append((a[k], a[j]))
print(target,':',p)