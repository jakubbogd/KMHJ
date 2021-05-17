import unittest
import pandas as pd

"""
from backend.classes.DetailedEdge import DetailedEdge
from backend.classes.DetailedNode import DetailedNode
from backend.classes.Graph import Graph
"""
from KMHJ.backend.classes.DetailedEdge import DetailedEdge
from KMHJ.backend.classes.DetailedNode import DetailedNode
from KMHJ.backend.classes.Graph import Graph
from KMHJ.backend.MathFuncs.MathFunctions import solve_salesman_problem

"""
    Testowanie klasy MathFunctions
"""

class GraphTest(unittest.TestCase):

    # using objects

    # tests
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

        graph1 = Graph(detailed_nodes, detailed_edges, 3049390, True)

        path = [edge_2, edge_5, edge_4, edge_6]
        self.assertEqual(solve_salesman_problem(graph1), path)

    def test_should_find_solution_2(self):
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
        self.assertEqual(solve_salesman_problem(graph1), path)



if __name__ == '__main__':
    unittest.main()
