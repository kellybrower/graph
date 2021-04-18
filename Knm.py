#Graph/Knm.py
from Graph import Graph
from Draw import Draw

class Knm(Graph):
    """Complete n by m bipartite graph"""
    def __init__(self, n, m):
        super().__init__()
        for i in range(0,n):
            self.insert_vertex((0,i))
        for j in range(0,m):
            self.insert_vertex((1,j))
        self.PartA = [v for v in self.vertices() if v.element()[0] == 0]
        self.PartB = [v for v in self.vertices() if v.element()[0] == 1]
        for v in self.PartA:
            for u in self.PartB:
                self.insert_edge(v,u,(u.element(),v.element()))
                    
if __name__ == "__main__":
    K34 = Knm(3,4)
    for v in K34.vertices():
        print(v.element())
    for e in K34.edges():
        print(e.element())
    Draw(K34)
