N = int(input("Введите число: "))

odd_numbers = []
for i in range(1, N + 1):
    if i % 2 != 0:
        odd_numbers.append(i)

print(f"Список из нечётных чисел от одного до N: {odd_numbers}")