"""
DetailedEdge.py
=====================
moduł reprezentujący szczegółową krawędź.
"""
from KMHJ.backend.classes.DetailedNode import DetailedNode
# from backend.classes.DetailedNode import DetailedNode

class DetailedEdge:

    def __init__(self, detailed_node_1, detailed_node_2, travel_time, time_param, prod_param):
        self.__detailed_node_1 = detailed_node_1
        self.__detailed_node_2 = detailed_node_2
        self.__travel_time = travel_time
        self.__weight_to_1 = self.count_weight(self.__detailed_node_1, time_param, prod_param)
        self.__weight_to_2 = self.count_weight(self.__detailed_node_2, time_param, prod_param)

    def __repr__(self):
        return str(self.__detailed_node_1)+":"+str(self.__detailed_node_2)

    def get_detailed_node_1(self):
        return self.__detailed_node_1

    def get_detailed_node_2(self):
        return self.__detailed_node_2

    def get_travel_time(self):
        return self.__travel_time

    def get_weight_to_1(self):
        return self.__weight_to_1

    def get_weight_to_2(self):
        return self.__weight_to_2

    def set_weight_to_1(self, weight_to_1):
        self.__weight_to_1 = weight_to_1

    def set_weight_to_2(self, weight_to_2):
        self.__weight_to_2 = weight_to_2

    def count_weight(self, node_to, time_param, prod_param):
        """
        Metoda obliczająca wagę krawędzi na podstawie wierzchołka do któergo idziemy i parametrów.

        :param node_to: Wierzchołek, do którego idziemy
        :param time_param: Parametr czasu do wagi
        :param prod_param: Parametr produkcji do wagi
        :return: Waga obliczona ze wzoru
        """
        return time_param * self.__travel_time + prod_param * node_to.get_products()
