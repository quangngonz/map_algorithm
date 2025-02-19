import tabulate
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra_test(json_data, start):
    # Convert JSON data to NetworkX graph
    nodes = json_data['nodes']
    edges = json_data['edges']

    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(edges)

    distances = {node: float('infinity') for node in G.nodes}
    distances[start] = 0
    unvisited = set(G.nodes)
    
    while unvisited:
        current = min(unvisited, key=lambda node: distances[node])
        unvisited.remove(current)
        
        for neighbor in G.neighbors(current):
            weight = G[current][neighbor]['weight']
            distances[neighbor] = min(distances[neighbor], distances[current] + weight)



    # Print the distances
    table = []
    for node, distance in distances.items():
        table.append([node, distance])
    
    table_content = tabulate.tabulate(table, headers=["Node", "Distance"], tablefmt="simple_grid")
    
    return distances, table_content

def a_star_test(json_data, start, end, plot_expected_result=False):
    # Convert JSON data to NetworkX graph
    nodes = json_data['nodes']
    edges = json_data['edges']

    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(edges)

    path = nx.astar_path(G, start, end, weight='weight')
    length = nx.astar_path_length(G, start, end, weight='weight')

    if plot_expected_result:
        # Plot the path with matplotlib
        pos = nx.spring_layout(G)
        plt.figure()

        # Draw the nodes and edges
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')

        # Highlight the path
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='red')
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

        # Draw edge labels (weights)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.title(f"A* Path from {start} to {end} - Expected Length: {length:.2f}", pad=20)
        plt.show()

    return path, length
