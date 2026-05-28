K = int(input("Сдвиг: "))
lst = [1, 4, -3, 0, 10]
print(f"Изначальный список: {lst}")

for i in range(K):
    last = lst[-1]
    for j in range(len(lst) - 1, 0, -1):
        lst[j] = lst[j - 1]
    lst[0] = last

print(f"Сдвинутый список: {lst}")