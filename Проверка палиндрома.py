def is_palindrome(s):
    """
    Рекурсивная проверка, является ли строка палиндромом.
    """
    # Приводим к нижнему регистру и убираем пробелы
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    # Базовые случаи
    if len(s) <= 1:
        return True
    
    # Рекурсивный случай
    if s[0] != s[-1]:
        return False
    
    return is_palindrome(s[1:-1])

# Пример использования
if __name__ == "__main__":
    test_strings = ["А роза упала на лапу Азора", "racecar", "hello", "level"]
    for s in test_strings:
        result = is_palindrome(s)
        print(f"'{s}' -> {'палиндром' if result else 'не палиндром'}")
