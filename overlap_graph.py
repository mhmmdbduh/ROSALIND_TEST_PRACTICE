import networkx as nx 
import matplotlib.pyplot as plt
# Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
#Return: The adjacency list corresponding to O3 .You may return edges in any order.
file = open('rosalind_grph.txt', 'r')

def main():
    file_name = 'rosalind_grph.txt'
    with open(file_name, 'r') as file:
        dna_strings = read_fasta(file)
    print(answer(overlap_graph(dna_strings)))

def read_fasta(file):
    dna_strings = {}
    for line in file:
        if line.startswith('>'):
            dna_strings[line[1:].strip()] = ''
            dna = line[1:].strip()
        else:
            dna_strings[dna] += line.strip()
    return dna_strings

def overlap_graph(dna_strings):
    graph = []
    for dna1 in dna_strings:
        for dna2 in dna_strings:
            if dna1 != dna2 and dna_strings[dna1][-3:] == dna_strings[dna2][:3]:
                graph.append((dna1, dna2))
    return graph

def answer(graph):
    for edge in graph:
        # create txt file
        with open('answer.txt', 'a') as file:
            file.write(edge[0] + ' ' + edge[1] + '\n')
        print(edge[0] + ' ' + edge[1])           

def visualize(graph):
    G = nx.DiGraph()
    G.add_edges_from(graph)
    nx.draw_random(G, with_labels=True, font_size=5)
    plt.show()
visualize(overlap_graph(read_fasta(file)))
if __name__ == '__main__':
    main()

