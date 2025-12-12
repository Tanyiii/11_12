class TreeNode:
    """Узел бинарного дерева"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal(node, result=None):
    """Прямой обход (Preorder): узел → левое поддерево → правое поддерево"""
    if result is None:
        result = []
    
    if node:
        result.append(node.value)  # Посетить узел
        preorder_traversal(node.left, result)  # Левое поддерево
        preorder_traversal(node.right, result)  # Правое поддерево
    
    return result

def inorder_traversal(node, result=None):
    """Симметричный обход (Inorder): левое поддерево → узел → правое поддерево"""
    if result is None:
        result = []
    
    if node:
        inorder_traversal(node.left, result)  # Левое поддерево
        result.append(node.value)  # Посетить узел
        inorder_traversal(node.right, result)  # Правое поддерево
    
    return result

def postorder_traversal(node, result=None):
    """Обратный обход (Postorder): левое поддерево → правое поддерево → узел"""
    if result is None:
        result = []
    
    if node:
        postorder_traversal(node.left, result)  # Левое поддерево
        postorder_traversal(node.right, result)  # Правое поддерево
        result.append(node.value)  # Посетить узел
    
    return result

# Пример использования
if __name__ == "__main__":
    # Создаем бинарное дерево:
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    
    print("Бинарное дерево:")
    print("        1")
    print("       / \\")
    print("      2   3")
    print("     / \\   \\")
    print("    4   5   6")
    print()
    
    print("Прямой обход (Preorder):", preorder_traversal(root))
    print("Симметричный обход (Inorder):", inorder_traversal(root))
    print("Обратный обход (Postorder):", postorder_traversal(root))
