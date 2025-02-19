from unit_test.generate_graph import generate_data
from unit_test.result import a_star_test
import random

G = generate_data()

print(G)
results = {}

BASE_NODE = 0
END_NODE = random.choice(G['nodes'])

print(f"Start node: {BASE_NODE}")
print(f"End node: {END_NODE}")

# Implement A* pathfinding algorithm here

path, length = a_star_test(G, 0, END_NODE, plot_expected_result=True)
