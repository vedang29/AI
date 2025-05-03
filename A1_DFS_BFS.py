# Enter input Like this
# values = [
#     1,
#     2,
#     4,
#     8, None, None,
#     9, None, None,
#     5, None, None,
#     3,
#     6, None,
#     10,
#     11, None, None,
#     None,
#     7, None, None
# ]

from collections import deque

# Node class for Binary Tree
class Node:
    def __init__(self, value, left=None, right=None):  # Corrected constructor
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):  # Corrected __str__ method
        return "Node(" + str(self.value) + ")"

# Build the binary tree using pre-order input
def build_tree():
    value = input("Enter node value (or leave empty for None): ")
    if value == "":
        return None
    left = build_tree()
    right = build_tree()
    return Node(value, left, right)

# Breadth-First Search (Level-order traversal) - Recursive version
def bfs_recursive(queue):
    if not queue:
        return
    node = queue.popleft()
    print(node)
    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)
    bfs_recursive(queue)

# Depth-First Search (Pre-order traversal)
def dfs_recursive(node):
    if node is None:
        return
    print(node)
    dfs_recursive(node.left)
    dfs_recursive(node.right)

# Menu display
def menu():
    print("\nBinary Tree Traversal")
    print("1. Build Tree")
    print("2. Breadth-First Search (BFS - Level Order)")
    print("3. Depth-First Search (DFS - Pre Order)")
    print("4. Exit")

# Main loop
tree = None

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Enter the binary tree in pre-order format:")
        tree = build_tree()
    elif choice == "2":
        if tree:
            print("\nBFS Traversal:")
            queue = deque([tree])
            bfs_recursive(queue)
        else:
            print("Tree is not built yet.")
    elif choice == "3":
        if tree:
            print("\nDFS Traversal:")
            dfs_recursive(tree)
        else:
            print("Tree is not built yet.")
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")



# from collections import deque

# class Node:
# 	def _init_(self, value, left=None, right=None):
# 		self.value = value
# 		self.left = left
# 		self.right = right

# 	def _str_(self):
# 		return "Node(" + str(self.value) + ")"

# def build_tree():
# 	value = input("Enter node value (or leave empty for None): ")
# 	if value == "":
# 		return None
# 	left = build_tree()
# 	right = build_tree()
# 	return Node(value, left, right)

# def bfs_recursive(queue):
# 	if not queue:
# 		return
# 	node = queue.popleft()
# 	print(node)
# 	if node.left:
# 		queue.append(node.left)
# 	if node.right:
# 		queue.append(node.right)
# 	bfs_recursive(queue)

# def dfs_recursive(node):
# 	if node is None:
# 		return
# 	print(node)
# 	dfs_recursive(node.left)
# 	dfs_recursive(node.right)

# def menu():
# 	print("Binary Tree Traversal")
# 	print("1. Build Tree")
# 	print("2. Breadth-First Search (BFS - Level Order)")
# 	print("3. Depth-First Search (DFS - Pre Order)")
# 	print("4. Exit")

# tree = None

# while True:
# 	menu()
# 	choice = input("Enter your choice: ")

# 	if choice == "1":
# 		print("Enter the binary tree in pre-order format:")
# 		tree = build_tree()
# 	elif choice == "2":
# 		if tree:
# 			print("\nBFS Traversal:")
# 			queue = deque([tree])
# 			bfs_recursive(queue)
# 		else:
# 			print("Tree is not built yet.")
# 	elif choice == "3":
# 		if tree:
# 			print("\nDFS Traversal:")
# 			dfs_recursive(tree)
# 		else:
# 			print("Tree is not built yet.")
# 	elif choice == "4":
# 		print("Exiting program.")
# 		break
# 	else:
# 		print("Invalid choice. Please try again.")