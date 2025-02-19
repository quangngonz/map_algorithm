from unit_test.generate_graph import generate_data
from unit_test.result import dijkstra_test

G = generate_data()

print(G)
results = {}

BASE_NODE = 0

# Implement Dijkstra's algorithm here

distances, table_content = dijkstra_test(G, BASE_NODE)
print(distances)
print(table_content)
