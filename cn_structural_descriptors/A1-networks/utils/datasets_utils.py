import os
import networkx as nx
import matplotlib.pyplot as plt
# import pygraphviz as pgv

PATH_DIRECTORIES = ['model', 'real', 'toy']

def read_networks_dir(path):
    graphs = []
    for dir in PATH_DIRECTORIES:
        fpath = os.path.join(path, dir)
        graphs.extend(read_networks(fpath))
    return graphs

def read_networks(path):
    graphs = []
    for filename in os.listdir(path):
        if filename == 'airports_UW.net':
        # if filename == 'homorand_N1000_K4_0.net':
            fpath = os.path.join(path, filename)
            mygraph = nx.read_pajek(fpath)
            graphs.append(mygraph)
    return graphs

def show_graph(graph):
    plt.subplot(121)
    nx.draw(graph, pos=nx.spring_layout(graph), with_labels=True, font_weight='bold')
    plt.subplot(122)
    nx.draw(graph)

    plt.show()