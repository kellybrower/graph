#Graph/Knm.py
from Graph import Graph

class Knm(Graph):
    """Complete n by m bipartite graph"""
    def __init__(self, n, m):
        super().__init__()
        for i in range(1,n+1):
            self.insert_vertex(i)
        for j in range(n+1,n+m+1):
            self.insert_vertex(j)
        for v in self.vertices():
            for u in self.vertices():
                if v!=u:
                    self.insert_edge(v,u,(u.element(),v.element()))
                    
if __name__ == "__main__":
    K34 = Knm(3,4)
    for v in K34.vertices():
        print(v.element())
    for e in K34.edges():
        print(e.element())

