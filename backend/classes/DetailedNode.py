"""

@author: HG
"""


class DetailedNode:

    def __init__(self, label, x_coord, y_coord, products):
        self.__label = label
        self.__x_coord = x_coord
        self.__y_coord = y_coord
        self.__products = products
        self.__entrance_products = products

    def get_entrance_products(self):
        return self.__entrance_products

    def get_label(self):
        return self.__label

    def get_x_coord(self):
        return self.__x_coord

    def get_y_coord(self):
        return self.__y_coord

    def get_products(self):
        return self.__products

    def set_label(self, label):
        self.__label = label

    def set_x_coord(self, x_coord):
        self.__x_coord = x_coord

    def set_y_coord(self, y_coord):
        self.__y_coord = y_coord

    def set_products(self, products):
        self.__products = products
    
    def get_k_value_to_node(self,graph):
         edges_list = graph.get_edges_to_node(self)
         min_time=min([edge.get_travel_time() for edge in edges_list])
         """ 
         for edge in edges_list:
             if edge.get_travel_time()<min_time:
                 min_time=edge.get_travel_time()
         """
         return self.get_products()/min_time       
