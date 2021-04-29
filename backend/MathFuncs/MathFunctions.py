from KMHJ.backend.classes.DetailedNode import DetailedNode


# TODO rozbic dijkstre na mniejsze funkcje


def dijkstra_algorithm(graph, start_node, end_node):
    """

    :param graph: graf realizujacy mape
    :param start_node: miasto startowe
    :param end_node: miasto koncowe
    :return: najdrozsza sciezka miedzy start_node a end_node
    """

    # -1 wystarcza bo wagi >0
    distances = {node: -1 for node in graph.get_detailed_nodes()}
    previous = {node: None for node in graph.get_detailed_nodes()}
    not_visited = [node for node in graph.get_detailed_nodes()]

    distances[start_node] = 0
    while len(not_visited) != 0:
        tmp_dist = {}
        for el in distances:
            if el in not_visited:
                #print(el.get_label() + " is not visited, set tmp_dist = " + str(distances[el]))
                tmp_dist[el] = distances[el]

        u = max(tmp_dist, key=tmp_dist.get)
        #print("set next_vert = " + u.get_label())
        not_visited.remove(u)
        #print("now not_visited is " + str([node.get_label() for node in not_visited]))
        neighbours_u = graph.get_neighbours(u)

        # dla sasiadow u:
        for element in neighbours_u:
            if element in not_visited:
                #print(element.get_label() + " is member of neighbours")
                #print("cost to " + element.get_label() + " is " + str(neighbours_u[element]))
                #print("element is" + element.get_label())
                if distances[element] < distances[u] + neighbours_u[element]:
                    #print("change element in path")
                    distances[element] = distances[u] + neighbours_u[element]
                    #print("distances of " + element.get_label() + " is now = " + str(distances[element]))
                    previous[element] = u
                    #print("previous of " + element.get_label() + " is now = " + str(u.get_label()))

    vertices_in_result = []
    node_to_append = end_node
    #print("end node is " + end_node.get_label())
    while node_to_append is not None:
        #print("append node " + node_to_append.get_label())
        vertices_in_result.append(node_to_append)
        node_to_append = previous[node_to_append]

    result = []
    for i in range(len(vertices_in_result) - 1):
        result.append(graph.find_edge_from_nodes(vertices_in_result[i], vertices_in_result[i + 1]))

    return result


def solve_salesman_problem(graph):
    """

    :param graph: graf realizujacy mapę
    :return: sciezka rozwiazująca problem wedrownego sprzedawcy
    """

    time = graph.get_worker_time()
    print("Calkowity czas sprzedawcy: " + str(time))

    start_node = graph.get_starting_node()

    not_visited = [node for node in graph.get_detailed_nodes()]
    not_visited.remove(start_node)

    path = []
    found_any = 1

    # szukam maksymalnych sciezek, poki moge
    while found_any == 1:
        print("Miasto począktkowe aktualnego obrotu: " + start_node.get_label())
        result = [res for res in algorithm_iteration(graph, start_node, time)]
        max_path = result[0]
        time = result[1]
        end_node = result[2]
        print("Do trasy dodaje krawedzie:")
        for edge in max_path:
            path.append(edge)
            if edge.get_detailed_node_1() in not_visited:
                not_visited.remove(edge.get_detailed_node_1())
            if edge.get_detailed_node_2() in not_visited:
                not_visited.remove(edge.get_detailed_node_2())
            print(edge.get_detailed_node_1().get_label() + "->" + edge.get_detailed_node_2().get_label())
        start_node = end_node
        if not max_path:
            found_any = 0

    print("Zostało czasu: " + str(time))
    for node in not_visited:
        print(node.get_label())
    # sprawdzam czy da sie jeszcze pojedyncze miasto dodac
    for node in not_visited:
        curr_edge_from_start = graph.find_edge_from_nodes(start_node, node)
        print("istnieje krawedz: " + curr_edge_from_start.get_detailed_node_1().get_label())
        if curr_edge_from_start and curr_edge_from_start.get_travel_time() <= time:
            path.append(edge)
            start_node = node
            time = time - curr_edge_from_start.get_travel_time()
            if node in not_visited:
                not_visited.remove(node)
        curr_edge_from_end = graph.find_edge_from_nodes(end_node, node)
        if curr_edge_from_end and curr_edge_from_end.get_travel_time() <= time:
            path.append(edge)
            end_node = node
            time = time - curr_edge_from_end.get_travel_time()
            if node in not_visited:
                not_visited.remove(node)

    return path


def algorithm_iteration(graph, start_node, time):
    max_path = []
    max_time = 0
    max_prod = 0
    end_node = []
    other_nodes = [node for node in graph.get_detailed_nodes()]
    other_nodes.remove(start_node)
    for node in other_nodes:
        curr_path = dijkstra_algorithm(graph, start_node, node)
        print("Kolejna ścieżka")
        curr_prod = 0
        curr_time = 0
        for edge in curr_path:
            curr_prod = curr_prod + edge.get_detailed_node_2().get_products()
            curr_time = curr_time + edge.get_travel_time()
        print("towarow sprzedanych na trasie: " + str(curr_prod))
        if curr_prod > max_prod and curr_time <= time:
            max_prod = curr_prod
            max_path = curr_path
            max_time = curr_time
            end_node = node
    if end_node:
        print("Wybrana trasa na ktorej sprzedano " + str(max_prod) + " towarow prowadzi do miasta " + end_node.get_label())

    return [max_path, time - max_time, end_node]
