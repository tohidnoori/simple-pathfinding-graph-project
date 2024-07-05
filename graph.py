import networkx as nx
import matplotlib.pyplot as plt

# Create a WAN graph with multiple areas
G = nx.Graph()

# Adding nodes for Area 1 (Safe Area)
G.add_node('A1-G', label='Gateway', area='Safe')
G.add_node('A1-1', label='Node', area='Safe')
G.add_node('A1-2', label='Node', area='Safe')
G.add_node('A1-3', label='Node', area='Safe')

# Adding nodes for Area 2 (Unsafe Area)
G.add_node('A2-G', label='Gateway', area='Unsafe')
G.add_node('A2-1', label='Node', area='Unsafe')
G.add_node('A2-2', label='Node', area='Unsafe')
G.add_node('A2-3', label='Node', area='Unsafe')

# Adding nodes for Area 3 (Safe Area)
G.add_node('A3-G', label='Gateway', area='Safe')
G.add_node('A3-1', label='Node', area='Safe')
G.add_node('A3-2', label='Node', area='Safe')
G.add_node('A3-3', label='Node', area='Safe')

# Adding edges for Area 1 (Safe Area)
G.add_edges_from([('A1-G', 'A1-1'), ('A1-G', 'A1-2'), ('A1-G', 'A1-3'),
                  ('A1-1', 'A1-2'), ('A1-1', 'A1-3'), ('A1-2', 'A1-3')])

# Adding edges for Area 2 (Unsafe Area)
G.add_edges_from([('A2-G', 'A2-1'), ('A2-G', 'A2-2'), ('A2-G', 'A2-3'),
                  ('A2-1', 'A2-2'), ('A2-2', 'A2-3')])

# Adding edges for Area 3 (Safe Area)
G.add_edges_from([('A3-G', 'A3-1'), ('A3-G', 'A3-2'), ('A3-G', 'A3-3'),
                  ('A3-1', 'A3-2'), ('A3-1', 'A3-3'), ('A3-2', 'A3-3')])

# Connecting Gateway nodes to simulate WAN connections
G.add_edges_from([('A1-G', 'A2-G'), ('A1-G', 'A3-G'), ('A2-G', 'A3-G')])

# Draw the graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)  # positions for all nodes

# Draw nodes with different colors for safe and unsafe areas
node_colors = ['lightblue' if G.nodes[node]['area'] == 'Safe' else 'lightcoral' for node in G]
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=700)

# Draw edges
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=2)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

# Show the plot
plt.title('Example WAN Graph with Safe and Unsafe Areas')
plt.show()

