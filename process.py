import os
# Import packages for data visualization
import plotly.offline as py
import plotly.graph_objects as go
import networkx as nx
#import matplotlib.pyplot as plt

G = nx.Graph()

class Node:

    def __init__(self, f):
        self.name = f
        self.lines = []
        self.outgoing_edges = 0
        self.incoming_edges = 0

    def update_lines(self):
        print("Updating lines")
        

# Take filename and return node object for file #
def add_nodes():

    directory = "text_docs/Notes/"
    for file in os.listdir(directory):
        f = os.fsdecode(file)
        print("Adding...")
        print(os.path.join(directory, f))
        print(f)
        curr = Node(f)
        G.add_node(curr)
        continue

def main():
    add_nodes()

if __name__ == "__main__":
    main()
