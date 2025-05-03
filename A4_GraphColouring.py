# SHORTER VERSION Added branch and bound to the code
# This program implements a simple graph coloring algorithm using a branch and bound approach.

def is_valid(node, color, assign, graph):
    return all(assign.get(nei) != color for nei in graph[node])

def bnb(assign, graph, colors, min_used, best):
    if len(assign) == len(graph):
        used = set(assign.values())
        if len(used) < min_used[0]:
            min_used[0] = len(used)
            best.clear()
            best.update(assign)
        return

    node = next(n for n in graph if n not in assign)
    for color in colors:
        if is_valid(node, color, assign, graph):
            assign[node] = color
            if len(set(assign.values())) <= min_used[0]:
                bnb(assign, graph, colors, min_used, best)
            assign.pop(node)

def solve(graph, colors):
    assign, best = {}, {}
    bnb(assign, graph, colors, [len(colors) + 1], best)
    return best or None

def input_graph_colors():
    graph = {}
    nodes = input("Enter node names (space-separated): ").split()
    for node in nodes:
        graph[node] = input(f"Enter neighbors of {node} (space-separated): ").split()
    colors = input("Enter colors (space-separated): ").split()
    return graph, colors

# Menu loop
graph = colors = result = None
while True:
    print("\n--- Graph Coloring Menu ---")
    print("1. Input Graph & Colors")
    print("2. Solve")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()
    if choice == '1':
        graph, colors = input_graph_colors()
    elif choice == '2':
        if graph and colors:
            result = solve(graph, colors)
            if result:
                print("\nColor Assignment:")
                for node, color in result.items():
                    print(f"{node}: {color}")
                print(f"Colors Used: {len(set(result.values()))} / {len(colors)}")
            else:
                print("No valid coloring found.")
        else:
            print("Please input the graph and colors first.")
    elif choice == '3':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")


# def is_valid(node, col, assign, graph):
#     for nei in graph[node]:
#         if nei in assign and assign[nei] == col:
#             return False
#     return True

# def bnb(assign, graph, cols, min_used, best):
#     if len(assign) == len(graph):
#         used = set(assign.values())
#         if len(used) < min_used[0]:
#             min_used[0] = len(used)
#             best.clear()
#             best.update(assign)
#         return

#     for node in graph:
#         if node not in assign:
#             break

#     for col in cols:
#         if is_valid(node, col, assign, graph):
#             assign[node] = col
#             if len(set(assign.values())) <= min_used[0]:
#                 bnb(assign, graph, cols, min_used, best)
#             del assign[node]

# def solve(graph, cols):
#     assign = {}
#     min_used = [len(cols) + 1]
#     best = {}
#     bnb(assign, graph, cols, min_used, best)
#     return best if best else None

# def input_graph():
#     n = int(input("Enter number of nodes: "))
#     graph = {}
#     print("Enter node names:")
#     nodes = [input("Node " + str(i+1) + ": ") for i in range(n)]
#     for node in nodes:
#         graph[node] = input("Enter neighbors of " + node + " (space-separated): ").split()
#     return graph, nodes

# def input_colors():
#     m = int(input("Enter number of colors: "))
#     return [input("Color " + str(i+1) + ": ") for i in range(m)]

# # Initialize variables
# graph = {}
# colors = []
# result = {}

# # Menu loop
# while True:
#     print("\n--- Graph Coloring Menu ---")
#     print("1. Add Graph")
#     print("2. Solve with Branch and Bound")
#     print("3. Exit")

#     ch = input("Enter your choice: ")

#     if ch == '1':
#         graph, nodes = input_graph()
#         colors = input_colors()  # Gather colors directly here
#     elif ch == '2':
#         if graph and colors:  # Check if both graph and colors are provided
#             result = solve(graph, colors)
#             if result:
#                 print("\nColor Assignment:")
#                 for node, col in result.items():
#                     print(node + ": " + col)
#                 print("Colors Used: " + str(len(set(result.values()))) + " / " + str(len(colors)))
#             else:
#                 print("No valid coloring found.")
#         else:
#             print("Graph or colors not provided. Please add them first.")
#     elif ch == '3':
#         print("Exiting...")
#         break
#     else:
#         print("Invalid choice. Try again.")
