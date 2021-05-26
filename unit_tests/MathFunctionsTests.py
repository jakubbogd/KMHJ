import unittest
import pandas as pd

# from KMHJ.GUI.files import ReadFiles
from GUI.files import ReadFiles

"""
from backend.classes.DetailedEdge import DetailedEdge
from backend.classes.DetailedNode import DetailedNode
from backend.classes.Graph import Graph
"""

"""
from KMHJ.backend.classes.DetailedEdge import DetailedEdge
from KMHJ.backend.classes.DetailedNode import DetailedNode
from KMHJ.backend.classes.Graph import Graph
from KMHJ.backend.MathFuncs.MathFunctions import solve_salesman_problem, algorithm_iteration, dijkstra_algorithm
"""
from backend.classes.DetailedEdge import DetailedEdge
from backend.classes.DetailedNode import DetailedNode
from backend.classes.Graph import Graph
from backend.MathFuncs.MathFunctions import solve_salesman_problem, algorithm_iteration, dijkstra_algorithm

"""
    Testowanie klasy MathFunctions
"""


class MathFunctionsTest(unittest.TestCase):

    # using objects

    # tests
    """
    Testy dla algorytmy Dijkstry
    """

    def test_should_return_correct_path_1(self):
        #pamietajmy ze wagami krawedzi są te obliczone wg naszego algorytmu
        #A zatem dla ułatwienia weźmy time_param = 1 i prod_param = 0 i będziemy mieli jako wagę po prostu długość trasy (waga będzie teraz symetryczna)
        #nie zmienia to merytoryki sprawdzania, a ułatwia rozumowanie
        vert_1 = DetailedNode("Marta", 1, 1, 20)
        vert_2 = DetailedNode("Kuba", 7, 7, 10)
        vert_3 = DetailedNode("Krzysio", 10, 12, 10)
        vert_4 = DetailedNode("Hubix", -5, 2, 10)
        vert_5 = DetailedNode("Legia", -5, 7, 22)
        detailed_nodes = [vert_1, vert_2, vert_3, vert_4, vert_5]
        edge_1 = DetailedEdge(vert_1, vert_2, 25, 1, 0)
        edge_2 = DetailedEdge(vert_2, vert_3, 20, 1, 0)
        edge_3 = DetailedEdge(vert_3, vert_4, 10, 1, 0)
        edge_4 = DetailedEdge(vert_4, vert_1, 20, 1, 0)
        edge_5 = DetailedEdge(vert_1, vert_3, 50, 1, 0)
        edge_6 = DetailedEdge(vert_5, vert_4, 20, 1, 0)
        edge_7 = DetailedEdge(vert_5, vert_3, 2, 1, 0)

        detailed_edges = [edge_1, edge_2, edge_3, edge_4, edge_5, edge_6, edge_7]

        graph_1 = Graph(detailed_nodes, detailed_edges, 10000, True)

        result = dijkstra_algorithm(graph_1, vert_2, vert_5) #ścieżka powinna być 2-1-3-4-5, sprawdzone recznie
        self.assertEqual(set(result), set([edge_1, edge_5, edge_3, edge_6]))

    def test_should_return_correct_path_2(self):
        #analogicznie 1-0 jak we wcześniejszym przykladzie
        vert_1 = DetailedNode("Marta", 1, 1, 20)
        vert_2 = DetailedNode("Kuba", 7, 7, 10)
        vert_3 = DetailedNode("Krzysio", 10, 12, 10)
        vert_4 = DetailedNode("Hubix", -5, 2, 10)
        vert_5 = DetailedNode("Legia", -5, 7, 22)
        detailed_nodes = [vert_1, vert_2, vert_3, vert_4, vert_5]
        edge_1 = DetailedEdge(vert_1, vert_2, 25, 1, 0)
        edge_2 = DetailedEdge(vert_2, vert_3, 20, 1, 0)
        edge_3 = DetailedEdge(vert_3, vert_4, 10, 1, 0)
        edge_4 = DetailedEdge(vert_4, vert_1, 20, 1, 0)
        edge_5 = DetailedEdge(vert_1, vert_3, 50, 1, 0)
        edge_6 = DetailedEdge(vert_5, vert_4, 20, 1, 0)
        edge_7 = DetailedEdge(vert_5, vert_3, 2, 1, 0)

        detailed_edges = [edge_1, edge_2, edge_3, edge_4, edge_5, edge_6, edge_7]

        graph_1 = Graph(detailed_nodes, detailed_edges, 10000, True)
        result = dijkstra_algorithm(graph_1, vert_1, vert_3)  # ścieżka powinna być 1-3, to po prostu krawedz, sprawdzone recznie
        self.assertEqual(set(result), set([edge_5]))

    """
    Testowanie funkcji solve_salesman_problem
    """

    def test_should_find_solution_1(self):
        vert_1 = DetailedNode("Marta", 1, 1, 20)
        vert_2 = DetailedNode("Kuba", 7, 7, 10)
        vert_3 = DetailedNode("Krzysio", 10, 12, 10)
        vert_4 = DetailedNode("Hubix", -5, 2, 10)
        vert_5 = DetailedNode("Legia", -5, 7, 22)
        detailed_nodes = [vert_1, vert_2, vert_3, vert_4, vert_5]
        edge_1 = DetailedEdge(vert_1, vert_2, 25, 0.5, 0.5)
        edge_2 = DetailedEdge(vert_2, vert_3, 20, 0.5, 0.5)
        edge_3 = DetailedEdge(vert_3, vert_4, 10, 0.5, 0.5)
        edge_4 = DetailedEdge(vert_4, vert_1, 20, 0.5, 0.5)
        edge_5 = DetailedEdge(vert_1, vert_3, 50, 0.5, 0.5)
        edge_6 = DetailedEdge(vert_5, vert_4, 20, 0.5, 0.5)
        edge_7 = DetailedEdge(vert_5, vert_3, 2, 0.5, 0.5)

        detailed_edges = [edge_1, edge_2, edge_3, edge_4, edge_5, edge_6, edge_7]

        graph1 = Graph(detailed_nodes, detailed_edges, 10000, True)

        path = [edge_2, edge_5, edge_4, edge_6]
        self.assertEqual(solve_salesman_problem(graph1, []), path)

    def test_should_find_solution_2(self):
        vert_1 = DetailedNode("Marta", 1, 1, 20)
        vert_2 = DetailedNode("Kuba", 7, 7, 10)
        vert_3 = DetailedNode("Krzysio", 10, 12, 10)
        vert_4 = DetailedNode("Hubix", -5, 2, 10)
        vert_5 = DetailedNode("Legia", -5, 7, 22)
        detailed_nodes = [vert_1, vert_2, vert_3, vert_4, vert_5]
        edge_1 = DetailedEdge(vert_1, vert_2, 25, 0.5, 0.5)
        edge_2 = DetailedEdge(vert_2, vert_3, 20, 0.5, 0.5)
        edge_3 = DetailedEdge(vert_3, vert_4, 10, 0.5, 0.5)
        edge_4 = DetailedEdge(vert_4, vert_1, 20, 0.5, 0.5)
        edge_5 = DetailedEdge(vert_1, vert_3, 50, 0.5, 0.5)
        edge_6 = DetailedEdge(vert_5, vert_4, 20, 0.5, 0.5)
        edge_7 = DetailedEdge(vert_5, vert_3, 2, 0.5, 0.5)

        detailed_edges = [edge_1, edge_2, edge_3, edge_4, edge_5, edge_6, edge_7]

        graph1 = Graph(detailed_nodes, detailed_edges, 100, True)

        path = [edge_5, edge_4, edge_6]
        self.assertEqual(solve_salesman_problem(graph1, []), path)

    def test_should_find_solution_3(self):
        vert_a = DetailedNode("a", 2, 3, 3)
        vert_b = DetailedNode("b", 2, 2, 5)
        vert_c = DetailedNode("c", 1, 1, 6)
        vert_d = DetailedNode("d", 3, 1, 1)

        detailed_nodes = [vert_a, vert_b, vert_c, vert_d]
        edge_ab = DetailedEdge(vert_a, vert_b, 4, 0.5, 0.5)
        edge_ac = DetailedEdge(vert_a, vert_c, 5, 0.5, 0.5)
        edge_bc = DetailedEdge(vert_b, vert_c, 1, 0.5, 0.5)
        edge_cd = DetailedEdge(vert_c, vert_d, 7, 0.5, 0.5)

        detailed_edges = [edge_ab, edge_ac, edge_bc, edge_cd]

        graph1 = Graph(detailed_nodes, detailed_edges, 33, True)

        path = [edge_ab, edge_ac, edge_cd, edge_bc]

        self.assertEqual(solve_salesman_problem(graph1, []), path)

    def test_should_find_solution_4(self):
        file1 = "1huge.csv"
        file2 = "2huge.csv"
        file3 = "3huge.csv"

        dfs = ReadFiles([file1, file2, file3, ""])

        graph = Graph([], [], None, None)
        graph.set_nodes_from_file(dfs[0])
        for node in graph.get_detailed_nodes():
            print(node.get_label())
        graph.set_edges_from_file(dfs[1])
        graph.set_worker_time(dfs[2].values.tolist()[0][0])
        graph.set_correct_edges_with_conditions()
        graph.set_start_node()

        edges = graph.get_detailed_edges()

        path = [edges[53], edges[41], edges[39], edges[36], edges[38], edges[43], edges[87], edges[68], edges[70], edges[76], edges[81], edges[86], edges[13]]

        self.assertEqual(solve_salesman_problem(graph, []), path)

    """
    Testowanie funkcji algorithm_iteration
    """
    def test_should_find_max_path(self):
        vert_a = DetailedNode("a", 2, 3, 3)
        vert_b = DetailedNode("b", 2, 2, 5)
        vert_c = DetailedNode("c", 1, 1, 6)
        vert_d = DetailedNode("d", 3, 1, 1)

        detailed_nodes = [vert_a, vert_b, vert_c, vert_d]
        edge_ab = DetailedEdge(vert_a, vert_b, 4, 0.5, 0.5)
        edge_ac = DetailedEdge(vert_a, vert_c, 5, 0.5, 0.5)
        edge_bc = DetailedEdge(vert_b, vert_c, 1, 0.5, 0.5)
        edge_cd = DetailedEdge(vert_c, vert_d, 7, 0.5, 0.5)

        detailed_edges = [edge_ab, edge_ac, edge_bc, edge_cd]

        graph1 = Graph(detailed_nodes, detailed_edges, 33, True)
        not_visited = [node for node in graph1.get_detailed_nodes()]
        not_visited.remove(vert_c)

        max_path = [edge_ab, edge_ac]

        result = [max_path, 24, vert_b, 14]
        self.assertEqual(algorithm_iteration(graph1, vert_c, not_visited, 33), result)


if __name__ == '__main__':
    unittest.main()
