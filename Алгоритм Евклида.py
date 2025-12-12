def gcd(a, b):
    """
    Рекурсивное вычисление НОД по алгоритму Евклида.
    """
    if b == 0:
        return a
    return gcd(b, a % b)

# Пример использования
if __name__ == "__main__":
    a, b = 48, 18
    result = gcd(a, b)
    print(f"НОД({a}, {b}) = {result}")
    # Проверка
    print(f"Проверка: {a} / {result} = {a // result}, {b} / {result} = {b // result}")
