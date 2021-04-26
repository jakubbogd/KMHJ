"""

@author: HG
"""
from backend.classes.DetailedNode import DetailedNode


class DetailedEdge:

    def __init__(self, node_1, node_2, detailed_node_1, detailed_node_2, travel_time, profit_to_node_1, profit_to_node_2, weight_to_1, weight_to_2):
        self.__node_1 = node_1
        self.__node_2 = node_2
        self.__detailed_node_1 = detailed_node_1
        self.__detailed_node_2 = detailed_node_2
        self.__travel_time = travel_time
        self.__profit_to_node_1 = profit_to_node_1
        self.__profit_to_node_2 = profit_to_node_2
        self.__weight_to_1 = weight_to_1
        self.__weight_to_2 = weight_to_2


    def get_node_1(self):
        return self.__node_1

    def get_node_2(self):
        return self.__node_2

    def get_detailed_node_1(self):
        return self.__detailed_node_1

    def get_detailed_node_2(self):
        return self.__detailed_node_2

    def get_travel_time(self):
        return self.__travel_time

    # Uzupelnic gettery i settery

    def count_weight(self, node_to, time_param, prod_param):
        return time_param * self.__travel_time + prod_param * node_to.get_products()
