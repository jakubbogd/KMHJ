from backend.classes.DetailedNode import DetailedNode

# TODO rozbic dijkstre na mniejsze funkcje


def dijkstra_algorithm(graph, start_node, end_node):
    """

    :param graph: graf realizujacy mape
    :param start_node: miasto startowe
    :param end_node: miastowe koncowe
    :return: najdrozsza sciezka miedzy start_node a end_node
    """

    # -10 wystarcza bo wagi >0
    distances = {node: -1 for node in graph.get_detailed_nodes()}
    previous = {node: None for node in graph.get_detailed_nodes()}
    not_visited = [node for node in graph.get_detailed_nodes()]

    distances[start_node] = 0
    while len(not_visited) != 0:
        tmp_dist = {}
        for el in distances:
            if el in not_visited:
                print(el.get_label() + " is not visited, set tmp_dist = " + str(distances[el]))
                tmp_dist[el] = distances[el]

        u = max(tmp_dist, key=tmp_dist.get)
        print("set next_vert = " + u.get_label())
        not_visited.remove(u)
        print("now not_visited is " + str([node.get_label() for node in not_visited]))
        neighbours_u = graph.get_neighbours(u)

        # dla sasiadow u:
        for element in neighbours_u:
            if element in not_visited:
                print(element.get_label() + " is member of neighbours")
                print("cost to " + element.get_label() + " is " +  str(neighbours_u[element]))
                print("element is" + element.get_label())
                if distances[element] < distances[u] + neighbours_u[element]:
                    print("change element in path")
                    distances[element] = distances[u] + neighbours_u[element]
                    print("distances of " + element.get_label() + " is now = " + str(distances[element]))
                    previous[element] = u
                    print("previous of " + element.get_label() + " is now = " + str(u.get_label()))

    vertices_in_result = []
    node_to_append = end_node
    print("end node is " + end_node.get_label())
    while node_to_append is not None:
        print("append node " + node_to_append.get_label())
        vertices_in_result.append(node_to_append)
        node_to_append = previous[node_to_append]

    result = []
    for i in range(len(vertices_in_result)-1):
        result.append(graph.find_edge_from_nodes(vertices_in_result[i], vertices_in_result[i+1]))

    return result


def solve_salesman_problem(graph):
    prod_param = 0.5
    time_param = 0.5

    Lista_sciezek = []
    miasto_poczatkowe = graph.get_starting_node()

    return Lista_sciezek
