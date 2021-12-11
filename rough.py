x, y, z, n = (int(input()) for _ in range(4))
li = []
for i in range(x + 1):
    print("value of i is", i)
    for j in range (y + 1):
        print("value of j is", j)
        for k in range (z + 1):
            print("value of k is", k)
            if i + j + k != n: #before printing the result, it will exclude the output which 'i' + 'j' + 'k' is the same as 'n'.
                li.append([i,j,k])
print(li)