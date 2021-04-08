import os
import re
# Import packages for data visualization
import plotly.offline as py
import plotly.graph_objects as go
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
labeldict = {}

class Node:

    def __init__(self, f):
        self.name = f
        self.lines = []
        self.outgoing_edges = 0
        self.incoming_edges = 0

    def update_lines(self):
        print("Updating lines")

regex = re.compile('see [also ]*note[s]* to[ lines]* [0-9]+[- ]*[0-9]*[ and]*[0-9]*')
regex2 = re.compile('[1-9]+[- ]*[0-9]*')

def parse_note(node):
    f = open("text_docs/Notes/" + node.name, 'r')
    for line in f:
        s = regex.findall(line)
        if s != []:
            print(s)
            for refs in s:
                e = regex2.findall(refs)
                print(e)
                for n in e:
                    new_node = Node(n + ".txt")
                    G.add_edge(node, new_node)
                    labeldict[new_node] = n
                    

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
        labeldict[curr] = (curr.name).replace(".txt", "")
        parse_note(curr)
        continue

def main():
    add_nodes()
    print(G.number_of_nodes())
    print(G.number_of_edges())
    nx.draw(G, labels=labeldict, with_labels = True)
    plt.show()

if __name__ == "__main__":
    main()
