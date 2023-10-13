for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print()

n = 4
sum = 0
for i in range(1, n + 1):
    sum += i

print(sum, "\n")

for i in range(7, 1, -1):
    for j in range(1, i - 1):
        print(j, end="")
    print()