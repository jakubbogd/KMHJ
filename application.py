"""
Wersja testowa, tu musi byc GUI i cała apka
"""
from GUI.files import GUI
from backend.classes.DetailedEdge import DetailedEdge
from backend.classes.DetailedNode import DetailedNode
from backend.classes.Graph import Graph
from backend.MathFuncs.MathFunctions import solve_salesman_problem, dijkstra_algorithm

if __name__ == "__main__":
    """# Przyklad na wczytywanie plikow z GUI, utworzenie na ich podstawie grafu i narysowanie go i sprawdzenie że krawędzie spełniają warunek nieprzecinania

    list_of_dfs = GUI()
    graph = Graph([], [], None, None)
    graph.set_nodes_from_file(list_of_dfs[0])
    for node in graph.get_detailed_nodes():
        print(node.get_label())
    graph.set_edges_from_file(list_of_dfs[1])
    graph.set_worker_time(list_of_dfs[2].values.tolist()[0][0])
    graph.plot_graph(True)
    #po rysunku widac ze krawedzie sa prawidlowe, ale sprawdzmy to
    graph.set_correct_edges_with_conditions()
    print("Get correct edges (should be true): " + str(graph.get_correct_edges()))"""

    # Przyklad ze rysowanie grafow dziala i że Dijkstra zwraca najdroższą ścieżkę (Jako wagi na razie przyjmuje czas)

    """"# Przyklad ze rysowanie grafow dziala
    vert_1 = DetailedNode("Marta", 1, 1, 20)
    vert_2 = DetailedNode("Kuba", 7, 7, 10)
    vert_3 = DetailedNode("Krzysio", 10, 12, 10)
    vert_4 = DetailedNode("Hubix", -5, 2, 10)
    vert_5 = DetailedNode("Legia", -5, 7, 22)

    detailed_nodes = [vert_1, vert_2, vert_3, vert_4, vert_5]
    edge_1 = DetailedEdge(vert_1.get_label(), vert_2.get_label(), vert_1, vert_2, 25, vert_1.get_products(), vert_2.get_products(), 1, 1)
    edge_2 = DetailedEdge(vert_2.get_label(), vert_3.get_label(), vert_2, vert_3, 20, vert_2.get_products(), vert_3.get_products(), 1, 1)
    edge_3 = DetailedEdge(vert_3.get_label(), vert_4.get_label(), vert_3, vert_4, 10, vert_3.get_products(), vert_4.get_products(), 1, 1)
    edge_4 = DetailedEdge(vert_4.get_label(), vert_1.get_label(), vert_4, vert_1, 20, vert_4.get_products(), vert_1.get_products(), 1, 2)
    edge_5 = DetailedEdge(vert_1.get_label(), vert_3.get_label(), vert_1, vert_3, 50, vert_1.get_products(), vert_3.get_products(), 1, 5)
    edge_6 = DetailedEdge(vert_5.get_label(), vert_4.get_label(), vert_5, vert_4, 20, vert_5.get_products(), vert_4.get_products(), 1, 2)
    edge_7 = DetailedEdge(vert_5.get_label(), vert_3.get_label(), vert_5, vert_3, 2, vert_5.get_products(), vert_3.get_products(), 1, 2)

    detailed_edges = [edge_1, edge_2, edge_3, edge_4, edge_5, edge_6, edge_7]

    graph = Graph(detailed_nodes, detailed_edges, 3049390, True)
    graph.plot_graph(True)

    #next = input("Jeśli chcesz wyswietlic graf ze sciezka wcisnij litere a i kliknij enter. Jesli nie - wcisnij cokolwiek innego i zatwierdz")
    """"""if next == "a":
        #path = [edge_1, edge_2, edge_3]
        path = solve_salesman_problem(graph)
        graph.plot_graph_with_path(path)""""""

    #Sprawdzam czy dziala dijkstra na grafie
    #na przykladzie Legia -- Krzysio. Powinno zwrocic najdrozsza jaka jest czyli Legia -- Hubi -- Marta -- Krzysio
    # sorki Kuba

    path = dijkstra_algorithm(graph, vert_5, vert_3)
    graph.plot_graph_with_path(path)

    # jeeeee bangla

    """
    """
    # Rysowanie grafu przykladowego gdzie krawedzie sie przecinaja i zwrocenie, ze warunek na correct edges jest False
    node_1 = DetailedNode("Wawa", 0, 0, 20)
    node_2 = DetailedNode("Krk", 3, 3, 10)
    node_3 = DetailedNode("Poznan", 3, 0, 10)
    node_4 = DetailedNode("Pruszkow", 0, 3, 10)

    edge_1 = DetailedEdge(node_1.get_label(), node_2.get_label(), node_1, node_2, 25, node_1.get_products(), node_2.get_products(), 1, 1)
    edge_2 = DetailedEdge(node_3.get_label(), node_4.get_label(), node_3, node_4, 25, node_3.get_products(), node_4.get_products(), 1, 1)

    detailed_nodes = [node_1, node_2, node_3, node_4]
    detailed_edges = [edge_1, edge_2]

    graph = Graph(detailed_nodes, detailed_edges, 3049390, None)
    graph.plot_graph(True)
    # po rysunku widac ze krawedzie sa prawidlowe, ale sprawdzmy to
    graph.set_correct_edges_with_conditions()
    print("Get correct edges (should be false): " + str(graph.get_correct_edges()))
    """
