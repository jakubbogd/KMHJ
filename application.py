"""
Wersja testowa, tu musi byc GUI i cała apka
"""


from backend.classes.DetailedEdge import DetailedEdge
from backend.classes.DetailedNode import DetailedNode
from backend.classes.Graph import Graph

if __name__ == "__main__":
    # Przyklad ze rysowanie grafow dziala
    vert_1 = DetailedNode("Marta", 1, 1, 20)
    vert_2 = DetailedNode("Kuba", 7, 7, 10)
    vert_3 = DetailedNode("Krzysio", 10, 12, 10)
    vert_4 = DetailedNode("Hubix", -5, 2, 10)
    vert_5 = DetailedNode("Legia", -5, 7, 22)

    detailed_nodes = [vert_1, vert_2, vert_3, vert_4, vert_5]
    edge_1 = DetailedEdge(vert_1.get_label(), vert_2.get_label(), 2, vert_1.get_products(), vert_2.get_products(), 1, 1)
    edge_2 = DetailedEdge(vert_2.get_label(), vert_3.get_label(), 2, vert_2.get_products(), vert_3.get_products(), 1, 1)
    edge_3 = DetailedEdge(vert_3.get_label(), vert_4.get_label(), 2, vert_3.get_products(), vert_4.get_products(), 1, 1)
    edge_4 = DetailedEdge(vert_4.get_label(), vert_1.get_label(), 2, vert_4.get_products(), vert_1.get_products(), 1, 1)
    edge_5 = DetailedEdge(vert_1.get_label(), vert_3.get_label(), 2, vert_1.get_products(), vert_3.get_products(), 1, 1)

    detailed_edges = [edge_1, edge_2, edge_3, edge_4, edge_5]

    graph = Graph(None, detailed_nodes, None, detailed_edges, 3049390, True)
    graph.plot_graph(True)

    next = input("Jeśli chcesz wyswietlic graf ze sciezka wcisnij litere a i kliknij enter. Jesli nie - wcisnij cokolwiek innego i zatwierdz")
    if next == "a":
        path = [edge_1, edge_2, edge_3]
        graph.plot_graph_with_path(path)
