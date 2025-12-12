def generate_permutations(s, start=0, result=None):
    """
    Генерация всех перестановок строки.
    """
    if result is None:
        result = []
    
    # Базовый случай: дошли до конца строки
    if start == len(s):
        result.append(''.join(s))
        return result
    
    # Рекурсивный случай
    for i in range(start, len(s)):
        # Меняем местами текущий символ с символом на позиции i
        s_list = list(s)
        s_list[start], s_list[i] = s_list[i], s_list[start]
        
        # Рекурсивный вызов для оставшейся части
        generate_permutations(s_list, start + 1, result)
        
        # Backtrack: возвращаем исходный порядок
        s_list[start], s_list[i] = s_list[i], s_list[start]
    
    return result

# Пример использования
if __name__ == "__main__":
    input_str = "abc"
    permutations = generate_permutations(input_str)
    print(f"Все перестановки строки '{input_str}':")
    for i, perm in enumerate(permutations, 1):
        print(f"{i:2}. {perm}")
    
    print(f"\nВсего перестановок: {len(permutations)} (ожидается {len(input_str)}! = {len(input_str)}!)")
