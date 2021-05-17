import unittest
import pandas as pd

from backend.classes.DetailedEdge import DetailedEdge
from backend.classes.DetailedNode import DetailedNode
from backend.classes.Graph import Graph

"""
    Testowanie klasy Graph
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

if __name__ == '__main__':
    unittest.main()
