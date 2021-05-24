import unittest
import pandas as pd

from backend.classes.DetailedEdge import DetailedEdge
from backend.classes.DetailedNode import DetailedNode
from backend.classes.Graph import Graph

"""
from KMHJ.backend.classes.DetailedEdge import DetailedEdge
from KMHJ.backend.classes.DetailedNode import DetailedNode
from KMHJ.backend.classes.Graph import Graph
"""

"""
    Testowanie klasy Graph i metody obliczającej wagę krawędzi z DetailedEdge
"""


def return_test_graph_1():
    vert_1 = DetailedNode("Marta", 1, 1, 20)
    vert_2 = DetailedNode("Kuba", 7, 7, 10)
    vert_3 = DetailedNode("Krzysio", 10, 12, 10)
    vert_4 = DetailedNode("Hubix", -5, 2, 10)
    vert_5 = DetailedNode("Legia", -5, 7, 22)
    detailed_nodes = [vert_1, vert_2, vert_3, vert_4, vert_5]
    edge_1 = DetailedEdge(vert_1, vert_2, 25, 0.5, 0.5)
    edge_2 = DetailedEdge(vert_2, vert_3, 20, 0.5, 0.5)
    edge_3 = DetailedEdge(vert_3, vert_4, 10, 0.5, 0.5)
    edge_4 = DetailedEdge(vert_4, vert_1, 20,  0.5, 0.5)
    edge_5 = DetailedEdge(vert_1, vert_3, 50, 0.5, 0.5)
    edge_6 = DetailedEdge(vert_5, vert_4, 20, 0.5, 0.5)
    edge_7 = DetailedEdge(vert_5, vert_3, 2,  0.5, 0.5)

    detailed_edges = [edge_1, edge_2, edge_3, edge_4, edge_5, edge_6, edge_7]

    graph1 = Graph(detailed_nodes, detailed_edges, 3049390, True)

    return graph1

"""
    Grafy do sprawdzania przecinania się krawedzi
"""
def return_test_graph_cross_edge_1():
    
    vert_1 = DetailedNode("Marta", 1, 1, 20)
    vert_2 = DetailedNode("Kuba", 5, 5, 10)
    vert_3 = DetailedNode("Krzysio", 1, 5, 10)
    vert_4 = DetailedNode("Hubix", 5, 1, 10)
    detailed_nodes = [vert_1, vert_2, vert_3, vert_4]
    edge_1 = DetailedEdge(vert_1, vert_2, 25, 0.5, 0.5)
    edge_2 = DetailedEdge(vert_3, vert_4, 20, 0.5, 0.5)
    detailed_edges = [edge_1, edge_2]
    graph1 = Graph(detailed_nodes, detailed_edges, 3049390, True)
    return graph1    

def return_test_graph_cross_edge_2():
    
    vert_1 = DetailedNode("Marta", 1, 5, 20)
    vert_2 = DetailedNode("Kuba", 1, -5, 10)
    vert_3 = DetailedNode("Krzysio", -2, 0, 10)
    vert_4 = DetailedNode("Hubix", 2 , 0, 10)
    detailed_nodes = [vert_1, vert_2, vert_3, vert_4]
    edge_1 = DetailedEdge(vert_1, vert_2, 25, 0.5, 0.5)
    edge_2 = DetailedEdge(vert_3, vert_4, 20, 0.5, 0.5)
    detailed_edges = [edge_1, edge_2]
    graph1 = Graph(detailed_nodes, detailed_edges, 3049390, True)         
    return graph1

def return_test_graph_cross_edge_3():
    vert_1 = DetailedNode("Marta", 0, 0, 20)
    vert_2 = DetailedNode("Kuba", 0, 5, 10)
    vert_3 = DetailedNode("Krzysio", 0, 3, 10)
    vert_4 = DetailedNode("Hubix", 0, 8, 10)
    detailed_nodes = [vert_1, vert_2, vert_3, vert_4]
    edge_1 = DetailedEdge(vert_1, vert_2, 25, 0.5, 0.5)
    edge_2 = DetailedEdge(vert_3, vert_4, 20, 0.5, 0.5) 
    detailed_edges = [edge_1, edge_2]
    graph1 = Graph(detailed_nodes, detailed_edges, 3049390, True)       
    return graph1
def return_test_graph_cross_edge_4(): 
    vert_1 = DetailedNode("Marta", 1, 1, 20)
    vert_2 = DetailedNode("Kuba", 5, 5, 10)
    vert_3 = DetailedNode("Krzysio", 3, 3, 10)
    vert_4 = DetailedNode("Hubix", 7, 7, 10)
    detailed_nodes = [vert_1, vert_2, vert_3, vert_4]
    edge_1 = DetailedEdge(vert_1, vert_2, 25, 0.5, 0.5)
    edge_2 = DetailedEdge(vert_3, vert_4, 20, 0.5, 0.5)   
    detailed_edges = [edge_1, edge_2]
    graph1 = Graph(detailed_nodes, detailed_edges, 3049390, True)     
    return graph1
def return_test_graph_cross_edge_5():
    vert_1 = DetailedNode("Marta", 0, 0, 20)
    vert_2 = DetailedNode("Kuba", 5, 0, 10)
    vert_3 = DetailedNode("Krzysio", 3, 0, 10)
    vert_4 = DetailedNode("Hubix", 7, 0, 10)
    detailed_nodes = [vert_1, vert_2, vert_3, vert_4]
    edge_1 = DetailedEdge(vert_1, vert_2, 25, 0.5, 0.5)
    edge_2 = DetailedEdge(vert_3, vert_4, 20, 0.5, 0.5)             
    detailed_edges = [edge_1, edge_2]
    graph1 = Graph(detailed_nodes, detailed_edges, 3049390, True)                  
    return graph1

class GraphTest(unittest.TestCase):

    # using objects

    # tests
    def test_should_create_graph_from_files(self):
        graph = Graph([], [], None, None)
        graph.set_nodes_from_file(pd.read_csv("1_old.csv"))
        for node in graph.get_detailed_nodes():
            print(node.get_label())
        graph.set_edges_from_file(pd.read_csv("2_old.csv"))
        graph.set_worker_time(pd.read_csv("3_old.csv").values.tolist()[0][0])
        self.assertTrue(len(graph.get_detailed_nodes()), 4)
        self.assertTrue(len(graph.get_detailed_edges()), 4)

    def test_should_find_index_correct(self):
        self.assertEqual(return_test_graph_1().find_detailed_node_index("Krzysio"), 2)

    def test_should_find_index_none(self):
        self.assertFalse(return_test_graph_1().find_detailed_node_index("Marcysia") is not None)

    def test_should_return_node_from_label(self):
        self.assertTrue(return_test_graph_1().get_node_from_label("Legia") is not None)

    def test_should_return_none_from_label(self):
        self.assertEqual(return_test_graph_1().get_node_from_label("Marcysia"), None)

    def test_should_return_correct_neighbours(self):
        graph = return_test_graph_1()
        verify = graph.get_detailed_nodes()[-1] # wierzchołek Legia ma dwóch sąsiadów
        self.assertTrue(len(graph.get_neighbours(verify).keys()) == 2)

    """
        Testy czy rozne rodzaje krawedzi ktore sie przecinaja to zwracane sa jako przecinajace sie krawedzie
    """
    def test_should_return_cross_edge1(self):
        graph = return_test_graph_cross_edge_1()
        verify = graph.set_correct_edges_with_conditions()
        self.assertTrue(verify==0)

    def test_should_return_cross_edge2(self):
        graph = return_test_graph_cross_edge_2()
        verify = graph.set_correct_edges_with_conditions()
        self.assertTrue(verify==0)

    def test_should_return_cross_edge3(self):
        graph = return_test_graph_cross_edge_3()
        verify = graph.set_correct_edges_with_conditions()
        self.assertTrue(verify==0)

    def test_should_return_cross_edge4(self):
        graph = return_test_graph_cross_edge_4()
        verify = graph.set_correct_edges_with_conditions()
        self.assertTrue(verify==0)

    def test_should_return_cross_edge5(self):
        graph = return_test_graph_cross_edge_5()
        verify = graph.set_correct_edges_with_conditions()
        self.assertTrue(verify==0)  
        
    def test_correct_k_value(self):
        graph=return_test_graph_1()
        verity = (graph.get_starting_node_with_max_k()).get_label()
        self.assertTrue(verity=="Legia")  
        
    def test_correct_k_value_for_node(self):
        graph=return_test_graph_1()
        verity = (graph.get_detailed_nodes()[0]).get_k_value_to_node(graph)
       
        self.assertTrue(verity==20/20)
        
    def test_should_return_unconnected_graph(self):
        graph=return_test_graph_cross_edge_1()
        verity=graph.check()
        self.assertTrue(not verity)
        
    def test_should_return_connected_graph(self):
        graph=return_test_graph_1()
        verity=graph.check()
        self.assertTrue( verity)      

    """
        Testy pozostałych funkcji z klasy Graph
    """

    def test_should_set_start_node(self):
        graph1 = return_test_graph_1()
        graph1.set_start_node()
        self.assertEqual(graph1.get_start_node().get_label(), "Legia")

    def test_should_find_solution(self):
        graph1 = return_test_graph_1()
        graph1.set_start_node()

        edges = graph1.get_detailed_edges()
        path = [edges[1], edges[4], edges[3], edges[5]]
        solution = ["Legia", "Hubix", "Marta", "Krzysio", "Kuba"]

        self.assertEqual(graph1.get_solution_from_path(path), solution)

    def test_should_not_find_solution(self):
        graph1 = return_test_graph_1()
        graph1.set_start_node()

        edges = graph1.get_detailed_edges()
        path = [edges[2], edges[5], edges[4], edges[6]]

        self.assertEqual(graph1.get_solution_from_path(path), [])

    def test_should_find_nodes(self):
        graph1 = return_test_graph_1()
        graph1.set_start_node()

        edges = graph1.get_detailed_edges()
        path = [edges[1], edges[4], edges[3], edges[5]]

        nodes = graph1.get_detailed_nodes()
        solution = [nodes[4], nodes[3], nodes[0], nodes[2], nodes[1]]

        self.assertEqual(graph1.get_nodes_from_path(path, nodes[4]), solution)

    def test_should_not_find_nodes_1(self):
        graph1 = return_test_graph_1()
        graph1.set_start_node()

        edges = graph1.get_detailed_edges()
        path = [edges[1], edges[4], edges[3], edges[5]]

        nodes = graph1.get_detailed_nodes()

        self.assertEqual(graph1.get_nodes_from_path(path, nodes[2]), [])

    def test_should_not_find_nodes_2(self):
        graph1 = return_test_graph_1()
        graph1.set_start_node()

        edges = graph1.get_detailed_edges()
        path = [edges[0], edges[2]]

        nodes = graph1.get_detailed_nodes()

        self.assertEqual(graph1.get_nodes_from_path(path, nodes[0]), [])

    def test_should_get_edges_from_node(self):
        graph1 = return_test_graph_1()
        graph1.set_start_node()

        nodes = graph1.get_detailed_nodes()

        self.assertEqual(len(graph1.get_edges_from_node(nodes[0])), 3)

    def test_should_find_edge_from_nodes_correct(self):
        graph_1 = return_test_graph_1()
        nodes = graph_1.get_detailed_nodes()

        node_1 = nodes[2]
        node_2 = nodes[3]
        result = graph_1.find_edge_from_nodes(node_1, node_2)

        self.assertTrue(result is not None)

    def test_should_find_edge_from_nodes_none(self):
        graph_1 = return_test_graph_1()
        nodes = graph_1.get_detailed_nodes()

        node_1 = nodes[0]
        node_2 = nodes[4]
        result = graph_1.find_edge_from_nodes(node_1, node_2)

        self.assertFalse(result is not None)

    def test_should_count_weight_in_edge_correct(self):
        graph_1 = return_test_graph_1()
        edges = graph_1.get_detailed_edges()
        nodes = graph_1.get_detailed_nodes()

        edge = edges[0]
        node_to = nodes[1]
        weight = edge.count_weight(node_to, 0.4, 0.6) # 0.4 * 25 + 0.6 * 10 = 10+6 = 16
        self.assertEqual(weight, 16)

if __name__ == '__main__':
    unittest.main()
