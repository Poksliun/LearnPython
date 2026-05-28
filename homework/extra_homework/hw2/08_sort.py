n = int(input("Количество чисел: "))
lst = []
for i in range(n):
    lst.append(int(input("Введите число: ")))

print(f"Изначальный список: {lst}")

for i in range(len(lst)):
    for j in range(len(lst) - 1 - i):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print(f"Отсортированный список: {lst}")