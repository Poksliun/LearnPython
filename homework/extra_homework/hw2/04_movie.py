films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']

n = int(input("Сколько фильмов хотите добавить? "))

favorites = []

for i in range(n):
    movie = input("Введите название фильма: ")
    if movie in films:
        favorites.append(movie)
    else:
        print(f"Ошибка: фильма {movie} у нас нет :(")

print(f"Ваш список любимых фильмов: {', '.join(favorites)}")