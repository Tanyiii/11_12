def solve_n_queens(n=8):
    """
    Решение задачи о расстановке N ферзей на доске N×N.
    Возвращает список всех решений.
    """
    def is_safe(board, row, col):
        """Проверка, можно ли поставить ферзя в позицию (row, col)"""
        # Проверка вертикали
        for i in range(row):
            if board[i] == col:
                return False
        
        # Проверка диагоналей
        for i in range(row):
            if abs(board[i] - col) == abs(i - row):
                return False
        
        return True
    
    def backtrack(board, row, solutions):
        """Рекурсивная функция backtracking"""
        # Базовый случай: все ферзи расставлены
        if row == n:
            solutions.append(board[:])
            return
        
        # Перебираем все столбцы для текущей строки
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col  # Ставим ферзя
                backtrack(board, row + 1, solutions)  # Рекурсивный вызов
                board[row] = -1   # Backtrack
    
    # Инициализация
    board = [-1] * n  # board[i] = столбец ферзя в строке i
    solutions = []
    
    backtrack(board, 0, solutions)
    return solutions

def print_solution(solution):
    """Красивая печать решения"""
    n = len(solution)
    for row in range(n):
        line = ""
        for col in range(n):
            line += "Q " if solution[row] == col else ". "
        print(line)
    print()

# Пример использования
if __name__ == "__main__":
    n = 8
    solutions = solve_n_queens(n)
    
    print(f"Задача о {n} ферзях:")
    print(f"Найдено решений: {len(solutions)}")
    
    # Покажем первые 2 решения
    print("\nПервые 2 решения:")
    for i in range(min(2, len(solutions))):
        print(f"Решение {i + 1}:")
        print_solution(solutions[i])
