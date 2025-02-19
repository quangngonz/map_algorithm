from unit_test.generate_graph import generate_data
from unit_test.result import a_star_test

G = generate_data()

print(G)
results = {}

BASE_NODE = 0
END_NODE = max(G['nodes'])

# Implement A* pathfinding algorithm here

path, length = a_star_test(G, 0, 5, plot_expected_result=True)
