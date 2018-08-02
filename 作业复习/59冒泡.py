a = [6,8,5,4,6,9,3,2]
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j]<a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)
