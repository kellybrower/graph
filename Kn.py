#Graph/Kn.py

from Graph import Graph
G = Graph()
def K_n(G,n=1):
    for i in range(1,n+1):
        G.insert_vertex(i)
    for v in G.vertices():
        for u in G.vertices():
            if v!=u:
                G.insert_edge(v, u)

if __name__ == "__main__":
    K_5 = Graph()
    K_n(K_5, 5)
    for e in K_5.edges():
        print(e)
        
