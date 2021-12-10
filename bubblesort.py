take = input("Please give your numbers for sorting\n")
process = [int(give) for give in str(take)]
print(process)
l = len(process)
print(l)
for i in range(l-1):
    for j in range(l-i-1):
        if process[j] > process[j+1]:
            process[j], process[j+1] = process[j+1], process[j]
print(*process)