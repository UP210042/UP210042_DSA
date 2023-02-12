a = [5,2,7,9,3]

for i in range(0, len(a)):
    print(a[i])

# Bubble sort
for i in range(0, len(a)+1 -2):
    for j in range(0,len(a)+1 - i-2):
        x = a[j]
        y = a[j+1]
        if x > y:
            a[j] = y
            a[j+1] = x

print(a)        