n = int(input("Количество контейнеров: "))

weights = []
for i in range(n):
    weight = int(input("Введите вес контейнера: "))
    while weight > 200:
        weight = int(input("Вес не должен превышать 200. Введите заново: "))
    weights.append(weight)

new_weight = int(input("Введите вес нового контейнера: "))
while new_weight > 200:
    new_weight = int(input("Вес не должен превышать 200. Введите заново: "))

position = 1
for w in weights:
    if new_weight <= w:
        position += 1
    else:
        break

print(f"Номер, который получит новый контейнер: {position}")