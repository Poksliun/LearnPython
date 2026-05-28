def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

def count_of_digits(n):
    return len(str(n))

n = int(input("Введите число: "))

summa = sum_of_digits(n)
count = count_of_digits(n)

print(f"Сумма чисел: {summa}")
print(f"Количество цифр в числе: {count}")
print(f"Разность суммы и количества цифр: {summa - count}")