lst = [4, 3, 2, 1]
x = 0
for i in range(len(lst)):
    for j in range(0, len(lst) - i - 1):
        x = x +1
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            continue
print(x)
