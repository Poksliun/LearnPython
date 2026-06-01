def bread(func):
    """Декоратор, добавляющий хлеб (Bread) сверху и снизу."""
    def wrapper():
        print("Bread")          # верхний кусок хлеба
        func()                  # вызов обёрнутой функции (внутренние слои)
        print("Bread")          # нижний кусок хлеба
    return wrapper

def salat(func):
    """Декоратор, добавляющий салат (Salat)."""
    def wrapper():
        print("Salat")
        func()
    return wrapper

def tomato(func):
    """Декоратор, добавляющий помидор (Tomato)."""
    def wrapper():
        print("Tomato")
        func()
    return wrapper

def meat(func):
    """Декоратор, добавляющий мясо (Meat)."""
    def wrapper():
        print("Meat")
        func()
    return wrapper

# Важно: декораторы применяются снизу вверх — порядок их перечисления влияет на очерёдность вывода
@bread
@salat
@tomato
@meat
def make_sandwich():
    """Базовая функция (ничего не делает)."""
    pass

def main():
    make_sandwich()

if __name__ == '__main__':
    main()