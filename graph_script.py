import pandas as pd
import networkx as nx
import json
import os

# Type colors
TYPE_COLOR_MAP = {
    'Normal': '#C4C4C4','Fire': "#F08030",'Water': "#4674E0",'Electric': "#FFEC5F",
    'Grass': '#78C850','Ice': '#98D8D8','Fighting': "#AA451A",'Poison': '#A040A0',
    'Ground': '#D4A85F','Flying': "#90B6F0",'Psychic': '#F85888','Bug': '#A8B820',
    'Rock': '#8B6F23','Ghost': '#705898','Dragon': '#7038F8','Dark': '#705848',
    'Steel': "#7F92A6",'Fairy': '#EE99AC', None: "#000000"
}

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "pokemon_data.csv")
df = pd.read_csv(csv_path, encoding="utf-8")

MAX_NODES = 1024
df = df.head(MAX_NODES)

G = nx.Graph()

for _, row in df.iterrows():
    name = row['display_name']
    type1 = row['type1'].replace('TYPE_', '').capitalize()
    type2 = row['type2'].replace('TYPE_', '').capitalize() if pd.notna(row['type2']) else None
    if type2 == type1:  # Only keep type2 if different
        type2 = None

    # Clean abilities
    ability1 = row.get('ability1')
    if pd.notna(ability1) and ability1 != "None":
        ability1 = " ".join(word.capitalize() for word in ability1.replace("ABILITY_", "").split("_"))
    else:
        ability1 = None

    ability2 = row.get('ability2')
    if pd.notna(ability2) and ability2 != "None" and ability2 != ability1:
        ability2 = " ".join(word.capitalize() for word in ability2.replace("ABILITY_", "").split("_"))
    else:
        ability2 = None

    G.add_node(name,
               id=row.get('id'),
               display_name=row['display_name'],
               type1=type1,
               type2=type2,
               color=TYPE_COLOR_MAP.get(type1,"#AAA"),
               size=10,
               sprite=row.get('sprite', ""),
               hp=row.get('hp'),
               attack=row.get('attack'),
               defense=row.get('defense'),
               special_attack=row.get('special_attack'),
               special_defense=row.get('special_defense'),
               speed=row.get('speed'),
               ability1=ability1,
               ability2=ability2,
               mondexentry=row.get('mondexentry')
              )

# Add edges for shared types
nodes = list(G.nodes)
for i, n1 in enumerate(nodes):
    for j in range(i+1,len(nodes)):
        n2 = nodes[j]
        types1 = {G.nodes[n1]['type1'], G.nodes[n1]['type2']}
        types2 = {G.nodes[n2]['type1'], G.nodes[n2]['type2']}
        if (types1 & types2) - {None}:
            G.add_edge(n1, n2, size=0.5)

# Compute fixed positions
pos = nx.spring_layout(G, seed=42, k=0.15, iterations=200)
for n in G.nodes:
    G.nodes[n]['x'] = float(pos[n][0])
    G.nodes[n]['y'] = float(pos[n][1])

# Map node keys to numeric IDs
node_id_map = {n: G.nodes[n]['id'] for n in G.nodes}

graph_data = {
    "nodes": [
        {**{"id": G.nodes[n]['id']}, **{k:v for k,v in G.nodes[n].items() if k != 'id'}}
        for n in G.nodes
    ],
    "edges": [
        {"id": f"{node_id_map[u]}-{node_id_map[v]}", 
         "source": node_id_map[u], 
         "target": node_id_map[v], 
         **G.edges[u,v]} 
        for u,v in G.edges
    ]
}

json_path = os.path.join(script_dir, "pokemon_graph_fixed.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(graph_data, f, indent=2)
