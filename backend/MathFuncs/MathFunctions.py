"""
MathFunctions.py
==================
Moduł zawierający definicje funkcji matematycznych.
"""
from KMHJ.backend.classes.DetailedNode import DetailedNode
# from backend.classes.DetailedNode import DetailedNode
from time import sleep


def dijkstra_algorithm(graph, start_node, end_node):
    """
    Funkcja realizująca zmodyfikowany algorytm Dijkstry (zmodyfikowany bo zwraca najdroższą ścieżkę a nie najtańszą).

    :param graph: graf realizujacy mape
    :param start_node: miasto startowe
    :param end_node: miasto koncowe
    :return: najdrozsza scieżka miedzy start_node a end_node
    """

    # -1 wystarcza bo wagi >0
    distances = {node: -1 for node in graph.get_detailed_nodes()}
    previous = {node: None for node in graph.get_detailed_nodes()}
    not_visited = [node for node in graph.get_detailed_nodes()]

    distances[start_node] = 0
    while len(not_visited) != 0: #dopoki są jeszcze nieodwiedzeni
        tmp_dist = {}
        for el in distances:
            if el in not_visited: #gdy coś jest nieodwiedzone doloz do tabeli distances z dijkstry
                tmp_dist[el] = distances[el]

        u = max(tmp_dist, key=tmp_dist.get) #weź maksymalną wartośc
        not_visited.remove(u)
        neighbours_u = graph.get_neighbours(u)

        # dla sasiadow u:
        for element in neighbours_u:
            if element in not_visited:
                # print(element.get_label() + " is member of neighbours")
                # print("cost to " + element.get_label() + " is " + str(neighbours_u[element]))
                # print("element is" + element.get_label())
                if distances[element] < distances[u] + neighbours_u[element]: # gdy wieksza odleglosc to podmien odleglosci - bo najwieksza sciezka
                    # print("change element in path")
                    distances[element] = distances[u] + neighbours_u[element]
                    # print("distances of " + element.get_label() + " is now = " + str(distances[element]))
                    previous[element] = u
                    # print("previous of " + element.get_label() + " is now = " + str(u.get_label()))

    vertices_in_result = []
    node_to_append = end_node
    # print("end node is " + end_node.get_label())
    while node_to_append is not None: # bierzemy wierzcholki do dodania juz do sciezki
        # print("append node " + node_to_append.get_label())
        vertices_in_result.append(node_to_append)
        node_to_append = previous[node_to_append]

    result = []
    for i in range(len(vertices_in_result) - 1): # bierzemy z wierzcholkow z rozwiazania tworzymy krawedzie
        result.append(graph.find_edge_from_nodes(vertices_in_result[i], vertices_in_result[i + 1]))

    return result


def solve_salesman_problem(graph, path_arg):
    """
    Funkcja zwracająca ścieżkę rozwiązującą problem wędrownego sprzedawcy zgodnie z opracowanych algorytmem.

    :param graph: graf realizujacy mapę
    :param path_arg: scieżka zachowująca obecnie stan rozwiązania
    :return: scieżka rozwiązująca problem wędrownego sprzedawcy
    """

    time = graph.get_worker_time()
    print("Calkowity czas sprzedawcy: " + str(time))

    # start_node = graph.get_starting_node()
    start_node = graph.get_starting_node_with_max_k()

    not_visited = [node for node in graph.get_detailed_nodes()]
    not_visited.remove(start_node)

    path = []
    found_any = 1
    prod_sold = 0
    # szukam maksymalnych sciezek, poki moge
    while found_any == 1:
        print("Miasto począktkowe aktualnego obrotu: " + start_node.get_label())
        result = [res for res in algorithm_iteration(graph, start_node, not_visited, time)]
        max_path = result[0]
        time = result[1]
        if result[2]:
            end_node = result[2]
        prod_sold = prod_sold + result[3]
        print("Do trasy dodaje krawedzie:")
        for edge in max_path:
            path.append(edge)
            path_arg.append(edge)
            edge.set_weight_to_1(0)
            edge.set_weight_to_2(0)
            edge.get_detailed_node_1().set_products(0)
            edge.get_detailed_node_2().set_products(0)
            if edge.get_detailed_node_1() in not_visited:
                not_visited.remove(edge.get_detailed_node_1())
            if edge.get_detailed_node_2() in not_visited:
                not_visited.remove(edge.get_detailed_node_2())
        start_node = end_node
        if not max_path:
            found_any = 0
        for edge in max_path:
            print(edge.get_detailed_node_1().get_label() + ": " + str(edge.get_weight_to_1()) + "->" + edge.get_detailed_node_2().get_label() + ": " + str(edge.get_weight_to_2()))

    #sleep(35.5)
    print("Zostało czasu: " + str(time))
    for node in not_visited:
        print(node.get_label())
    # sprawdzam czy da sie jeszcze pojedyncze miasto dodac
    print("Wierzchołek koncowy: " + end_node.get_label())
    for node in not_visited:
        curr_edge_from_end = graph.find_edge_from_nodes(end_node, node)
        if curr_edge_from_end and curr_edge_from_end.get_travel_time() <= time:
            print("Do rozwiazania dodano krawedz: " + curr_edge_from_end.get_detailed_node_1().get_label() + "->" + curr_edge_from_end.get_detailed_node_2().get_label())
            path.append(curr_edge_from_end)
            path_arg.append(curr_edge_from_end)
            end_node = node
            time = time - curr_edge_from_end.get_travel_time()
            if node in not_visited:
                not_visited.remove(node)
    print("Rozwiazaniem jest scieżka:")
    for edge in path:
        print(edge.get_detailed_node_1().get_label() + "->" + edge.get_detailed_node_2().get_label())
    print("przebyta w czasie " + str(graph.get_worker_time()-time) + " podczas, której sprzedano " + str(prod_sold) + " towarów")
    print("Funkcja solve_salesman_problem konczy dzialanie")
    return path


def algorithm_iteration(graph, start_node, not_visited, time):
    """
    Funkcja wykonująca jedną iterację algorytmu rozwiazujacego problem wędrownego sprzedawcy.
    Dla wskazanego wierzchołka początkowego konstruuje ścieżki o największych wagach do wszystkich nieodwiedzonych jeszcze wierzchołków i wybiera z nich tę o największej ilosciu produktów na niej sprzedanych.

    :param graph: graf realizujący mapę
    :param start_node: wierzchołek, z którego startuje obecna iteracja algorytmu
    :param not_visited: nieodwiedzone wierzchołki
    :param time: pozostały czas
    :return: lista składająca się ze scieżki będącej wynikiem jednej iteracji algorytmu, czasu pozostałego po jej przejściu, wierzchołka końcowego tej ścieżki i produktów podczas niej sprzedanych.
    """
    max_path = []
    max_time = 0
    max_prod = 0
    end_node = []
    for node in not_visited:
        curr_path = dijkstra_algorithm(graph, start_node, node)
        curr_time = 0
        for curr_edge in curr_path:
            curr_time = curr_time + curr_edge.get_travel_time()
        curr_prod = 0
        curr_nodes = graph.get_nodes_from_path(curr_path, start_node)
        for curr_node in curr_nodes:
            curr_prod = curr_prod + curr_node.get_products()

        if curr_prod > max_prod and curr_time <= time:
            max_prod = curr_prod
            max_path = curr_path
            max_time = curr_time
            end_node = node
    if end_node:
        print("Wybrano trasa na ktorej sprzedano " + str(max_prod) + " towarow w czasie " + str(max_time) + " prowadzi do miasta " + end_node.get_label())

    return [max_path, time - max_time, end_node, max_prod]
