#Graph/Draw.py

import matplotlib.pyplot as plt

def Draw(Graph):
    fig, ax = plt.subplots()
    for e in Graph.edges():
        ax.plot(e.element(), color='black', marker='o')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["top"].set_color("None")
    ax.spines["right"].set_color("None")
    ax.spines["bottom"].set_color("None")
    ax.spines["left"].set_color("None")
    plt.show()
        
    
