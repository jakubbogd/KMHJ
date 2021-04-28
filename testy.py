# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from backend.classes.DetailedEdge import DetailedEdge
from backend.classes.DetailedNode import DetailedNode
from backend.classes.Graph import Graph
from backend.MathFuncs.MathFunctions import solve_salesman_problem, dijkstra_algorithm

if __name__ == "__main__":
    # Przyklad ze rysowanie grafow dziala
    vert_1 = DetailedNode("Marta",-3 , -3, 20)
    vert_2 = DetailedNode("Kuba", 5, 0, 10)
    vert_3 = DetailedNode("Krzysio", 3, 2, 10)
    vert_4 = DetailedNode("Hubix", -2, -4, 10)
    vert_5 = DetailedNode("test 5", 1, 5, 10)
    vert_6 = DetailedNode("test 6", -2, -3, 10)

    detailed_nodes = [vert_1, vert_2, vert_3, vert_4, vert_5, vert_6]
    """
    edge_1 = DetailedEdge(vert_1.get_label(), vert_2.get_label(), vert_1, vert_2, 25, vert_1.get_products(), vert_2.get_products(), 1, 1)
    edge_2 = DetailedEdge(vert_2.get_label(), vert_3.get_label(), vert_2, vert_3, 20, vert_2.get_products(), vert_3.get_products(), 1, 1)
    edge_3 = DetailedEdge(vert_3.get_label(), vert_4.get_label(), vert_3, vert_4, 10, vert_3.get_products(), vert_4.get_products(), 1, 1)
    edge_4 = DetailedEdge(vert_4.get_label(), vert_1.get_label(), vert_4, vert_1, 20, vert_4.get_products(), vert_1.get_products(), 1, 2)
    edge_5 = DetailedEdge(vert_1.get_label(), vert_3.get_label(), vert_1, vert_3, 50, vert_1.get_products(), vert_3.get_products(), 1, 5)
    """ 
    edge_1 = DetailedEdge(vert_1.get_label(), vert_2.get_label(), vert_1, vert_2, 25, vert_1.get_products(), vert_2.get_products(), 1, 1)
    edge_2 = DetailedEdge(vert_3.get_label(), vert_4.get_label(), vert_3, vert_4, 20, vert_3.get_products(), vert_4.get_products(), 1, 1)
    edge_3 = DetailedEdge(vert_5.get_label(), vert_6.get_label(), vert_5, vert_6, 10, vert_5.get_products(), vert_6.get_products(), 1, 1)
    
    detailed_edges = [edge_1, edge_2, edge_3]

    graph = Graph(None, detailed_nodes, None, detailed_edges, 3049390, True)
    graph.plot_graph(True)
    if graph.check_correct_edges(edge_1, edge_2):
        print("powinno sie  wyswietlic krawedzie 1 i 2 ")
    if graph.check_correct_edges(edge_1, edge_3):
        print("powinno sie  wyswietlic krawedzie 1 i 3")   
    if graph.check_correct_edges(edge_2, edge_3):
        print("powinno sie nie wyswietlic krawedzie 2 i 3")   
