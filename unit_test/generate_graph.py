import networkx as nx
import matplotlib.pyplot as plt
import random
import json

def generate_graph(num_nodes=10, num_edges=15, weight_range=(1, 10)):
    G = nx.Graph()
    
    # Ensure all nodes have at least one connection
    nodes = list(range(num_nodes))
    random.shuffle(nodes)
    for i in range(num_nodes - 1):
        weight = random.randint(*weight_range)
        G.add_edge(nodes[i], nodes[i+1], weight=weight)
    
    # Add additional random edges
    edges = set(G.edges)
    while len(edges) < num_edges:
        u, v = random.sample(range(num_nodes), 2)
        if (u, v) not in edges and (v, u) not in edges:
            weight = random.randint(*weight_range)
            G.add_edge(u, v, weight=weight)
            edges.add((u, v))
    
    return G

def format_to_json(G):
    return {
        "nodes": list(G.nodes),
        "edges": [(u, v, G[u][v]['weight']) for u, v in G.edges]
    }

def save_graph(G, filename="graph.json"):
    graph_data = {
        "nodes": list(G.nodes),
        "edges": [(u, v, G[u][v]['weight']) for u, v in G.edges]
    }
    with open(filename, "w") as f:
        json.dump(graph_data, f, indent=4)

def draw_graph(G):
    pos = nx.spring_layout(G, seed=42)  # Consistent layout for better visuals
    labels = nx.get_edge_attributes(G, 'weight')
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='black', node_size=800, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')
    plt.show()

def generate_data():
    G = generate_graph()
    formatted_graph = format_to_json(G)
    save_graph(G)
    return formatted_graph

if __name__ == "__main__":
    G = generate_graph()
    formatted_graph = format_to_json(G)

    nodes = formatted_graph['nodes']
    edges = formatted_graph['edges']

    for node in nodes:
        print(node)

    for edge in edges:
        a_point, b_point, distance = edge
        print(a_point, b_point, distance)

    save_graph(G)
    draw_graph(G)
