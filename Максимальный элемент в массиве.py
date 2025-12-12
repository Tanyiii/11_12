def find_max(arr, index=0):
    """
    Рекурсивное нахождение максимального элемента в массиве.
 
    """
    # Базовый случай
    if index == len(arr) - 1:
        return arr[index]
    
    # Рекурсивный случай
    current = arr[index]
    rest_max = find_max(arr, index + 1)
    
    return current if current > rest_max else rest_max

# Пример использования
if __name__ == "__main__":
    arr = [3, 7, 2, 9, 1, 4, 6, 5, 8]
    result = find_max(arr)
    print(f"Массив: {arr}")
    print(f"Максимальный элемент: {result}")
    print(f"Проверка (встроенная функция): {max(arr)}")
