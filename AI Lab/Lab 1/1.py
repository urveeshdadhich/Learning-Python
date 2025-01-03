n = 7

#method 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

#method 2
for a in range(1, n+1):
    print(" *" * a)