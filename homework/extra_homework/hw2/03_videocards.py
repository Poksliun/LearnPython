n = int(input("Количество видеокарт: "))

gpus = []
for i in range(1, n + 1):
    gpu = int(input(f"{i} Видеокарта: "))
    gpus.append(gpu)

print(f"Старый список видеокарт: {gpus}")

max_gpu = max(gpus)
new_gpus = [gpu for gpu in gpus if gpu != max_gpu]

print(f"Новый список видеокарт: {new_gpus}")