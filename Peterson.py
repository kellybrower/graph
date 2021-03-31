#Peterson.py

from Graph import Graph

Peterson_vertices = [{'a','b'}, {'a','c'}, {'a','d'}, {'a','e'},
                     {'b','c'}, {'b','d'}, {'b','e'},
                     {'c','d'}, {'c','e'},
                     {'d','e'}]
class Peterson(Graph):
    def __init__(self):
        super().__init__()
        for u in Peterson_vertices:
            self.insert_vertex(u)
        for u in self.vertices():
            for v in self.vertices(): 
                if u.element().isdisjoint(v.element()):
                    self.insert_edge(u, v, 1)


if __name__ == "__main__":
    p = Peterson()
    for v in p.edges():
        print(v, v.element())
