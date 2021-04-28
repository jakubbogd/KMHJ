"""

@author: HG
"""

from backend.classes.DetailedNode import DetailedNode
from backend.classes.DetailedEdge import DetailedEdge
import matplotlib.pyplot as plt

plt.style.use("ggplot")

class Graph:

    def __init__(self, nodes, detailed_nodes, edges, detailed_edges, worker_time, correct_edges):
        self.__nodes = nodes
        self.__detailed_nodes = detailed_nodes
        self.__edges = edges
        self.__detailed_edges = detailed_edges
        self.__worker_time = worker_time
        self.__correct_edges = correct_edges

    # uzupełnione gettery i settery
    def get_nodes(self):
        return self.__nodes

    def get_detailed_nodes(self):
        return self.__detailed_nodes

    def get_edges(self):
        return self.__edges

    def get_detailed_edges(self):
        return self.__detailed_edges

    def get_worker_time(self):
        return self.__worker_time

    def get_correct_edges(self):
        return self.__correct_edges

    def set_nodes(self, nodes):
        self.__nodes = nodes

    def set_detailed_nodes(self, detailed_nodes):
        self.__detailed_nodes = detailed_nodes

    def set_edges(self, edges):
        self.__edges = edges

    def set_detailed_edges(self, detailed_edges):
        self.__detailed_edges = detailed_edges

    def set_worker_time(self, worker_time):
        self.__worker_time = worker_time

    def set_correct_edges(self, correct_edges):
        self.__correct_edges = correct_edges

    def get_starting_node(self):
        node = DetailedNode("Zero", 1, 1, 0)
        for n in self.__detailed_nodes:
            if node.get_products() < n.get_products():
                node = n
        return node

    def check_correct_edges(self, edge_1, edge_2):
        """

        :param edge_1: krawedz z klasy DetailedEdge
        :param edge_2: krawedz z klasy DetailedEdge
        :return: czy krawedzie spelniaja warunek nieprzecinania
        zwraca True jesli krawedzie sie przecinaja i False jesli krawedzie sie nie przecinaja
       
        """
        # przydaja mi sie takie rzeczy wiec na poczatek rzucilem 
        x1 = min(edge_1.get_detailed_node_1().get_x_coord(), edge_1.get_detailed_node_2().get_x_coord() )
        x2 = max(edge_1.get_detailed_node_1().get_x_coord(), edge_1.get_detailed_node_2().get_x_coord() )
        y1 = min(edge_1.get_detailed_node_1().get_y_coord(), edge_1.get_detailed_node_2().get_y_coord() )
        y2 = max(edge_1.get_detailed_node_1().get_y_coord(), edge_1.get_detailed_node_2().get_y_coord() )
        
        z1 = min(edge_2.get_detailed_node_1().get_x_coord(), edge_2.get_detailed_node_2().get_x_coord() )
        z2 = max(edge_2.get_detailed_node_1().get_x_coord(), edge_2.get_detailed_node_2().get_x_coord() )
        v1 = min(edge_2.get_detailed_node_1().get_y_coord(), edge_2.get_detailed_node_2().get_y_coord() )
        v2 = max(edge_2.get_detailed_node_1().get_y_coord(), edge_2.get_detailed_node_2().get_y_coord() )
        
        # przypadek gdy obie krawedzie sa pionowe
        if edge_1.get_detailed_node_1().get_x_coord() == edge_1.get_detailed_node_2().get_x_coord() and edge_2.get_detailed_node_1().get_x_coord() == edge_2.get_detailed_node_2().get_x_coord() :
            if x1 == z1 and min(y2,v2) > max(y1,v1):
                return True
            else:
                return False
        # przypadek gdy pierwsza krawedz jest "pionowa" 
        
        if edge_1.get_detailed_node_1().get_x_coord() == edge_1.get_detailed_node_2().get_x_coord() :
             if edge_2.get_detailed_node_1().get_y_coord() == edge_2.get_detailed_node_2().get_y_coord() :
                 a2=0
                 b2 = edge_2.get_detailed_node_1().get_y_coord()
             else:
                a2 = (edge_2.get_detailed_node_1().get_y_coord() - edge_2.get_detailed_node_2().get_y_coord() ) / (edge_2.get_detailed_node_1().get_x_coord() - edge_2.get_detailed_node_2().get_x_coord() )
                b2 = edge_2.get_detailed_node_1().get_y_coord() - a2* edge_2.get_detailed_node_1().get_x_coord()
            
             x = edge_1.get_detailed_node_1().get_x_coord()
             y = round(a2*x+b2,2)


             if  y > y1 and y < y2 and y>=v1 and y<=v2 :
                 print("Krawedzie  przecinaja sie w punkcie (",x,"," ,y,")")
                 return True
             else:
                 return False            
        
       # przypadek gdy druga krawedz jest "pionowa" 
        if edge_2.get_detailed_node_1().get_x_coord() == edge_2.get_detailed_node_2().get_x_coord() :
            if edge_1.get_detailed_node_1().get_y_coord() == edge_1.get_detailed_node_2().get_y_coord() :
                 a1=0
                 b1 = edge_1.get_detailed_node_1().get_y_coord()
            else:
                a1 = (edge_1.get_detailed_node_1().get_y_coord() - edge_1.get_detailed_node_2().get_y_coord() ) / (edge_1.get_detailed_node_1().get_x_coord() - edge_1.get_detailed_node_2().get_x_coord() )
                b1 = edge_1.get_detailed_node_1().get_y_coord() - a1* edge_1.get_detailed_node_1().get_x_coord()
            
            x = edge_2.get_detailed_node_1().get_x_coord()
            y = round(a1*x+b1,2)
       

            if  y >= y1 and y <= y2 and y>v1 and y<v2 :
                print("Krawedzie  przecinaja sie w punkcie (",x,"," ,y,")")
                return True
            else:
                 return False
    
       # dla pozostalych przypadkow 
           
        "wspolczynniki na prosta przechodzaca przez edge1"
        if edge_1.get_detailed_node_1().get_y_coord() == edge_1.get_detailed_node_2().get_y_coord() :
            a1=0
            b1 = edge_1.get_detailed_node_1().get_y_coord()
        else:
            a1 = (edge_1.get_detailed_node_1().get_y_coord() - edge_1.get_detailed_node_2().get_y_coord() ) / (edge_1.get_detailed_node_1().get_x_coord() - edge_1.get_detailed_node_2().get_x_coord() )
            b1 = edge_1.get_detailed_node_1().get_y_coord() - a1* edge_1.get_detailed_node_1().get_x_coord()
         
        "wspolczynniki na prosta przechodzaca przez edge2"
        if edge_2.get_detailed_node_1().get_y_coord() == edge_2.get_detailed_node_2().get_y_coord(): 
            a2=0
            b2 = edge_2.get_detailed_node_1().get_y_coord()
        else:
             a2 = (edge_2.get_detailed_node_1().get_y_coord() - edge_2.get_detailed_node_2().get_y_coord()) / (edge_2.get_detailed_node_1().get_x_coord() - edge_2.get_detailed_node_2().get_x_coord() )
             b2 = edge_2.get_detailed_node_1().get_y_coord() - a2* edge_2.get_detailed_node_1().get_x_coord()
        
        if abs(a1-a2)<0.0001 and abs(b1-b2)<0.0001: 
            return True
        
    #wspolrzedne punktu w ktorym sie proste przecinaja
        x = round((b2-b1)/(a1-a2) ,2)
        y = round(a2*x+b2,2)
                      
        if   x > x1 and x < x2 and y > y1 and y < y2 and x >z1 and x<z2 and y>v1 and y<v2 :
            print("Krawedzie  przecinaja sie w punkcie (",x,"," ,y,")")
            return True
        else:
            return False

    def set_nodes_from_file(self, file):
        """

        :param file: plik z ktorego tworzymy wierzcholki
        :return: chyba empty, bo ustawia odpowiednio wierzcholki
        """

    def set_edges_from_file(self, file):
        """

        :param file: plik z ktorego tworzymy krawedzie
        :return: chyba empty, bo ustawia odpowiednio wierzcholek
        """

    def plot_graph(self, show):
        xs = {node.get_label(): node.get_x_coord() for node in self.__detailed_nodes}
        ys = {node.get_label(): node.get_y_coord() for node in self.__detailed_nodes}
        for node in self.__detailed_nodes:
            plt.text(xs[node.get_label()], ys[node.get_label()], node.get_label(),fontsize=12, c="black")
            plt.plot(xs[node.get_label()], ys[node.get_label()], "bo")
        for edge in self.__detailed_edges:
            plt.plot([xs[edge.get_node_1()], xs[edge.get_node_2()]],
                     [ys[edge.get_node_1()], ys[edge.get_node_2()]], 'o--', color = "blue")
        plt.grid(True)
        if show:
            plt.show()

    def plot_graph_with_path(self, path):
        xs = {node.get_label(): node.get_x_coord() for node in self.__detailed_nodes}
        ys = {node.get_label(): node.get_y_coord() for node in self.__detailed_nodes}
        self.plot_graph(False)
        for edge in path:
            plt.plot([xs[edge.get_node_1()], xs[edge.get_node_2()]],
                 [ys[edge.get_node_1()], ys[edge.get_node_2()]], 'ro-')
        plt.show()

    def get_neighbours(self, node):
        """

        :param node: node which neighbours we are looking for
        :return: neighbours of node
        """
        # zwrot te krawedzie, ktore zawieraja node w sobie
        edges_with_node = [edge for edge in self.__detailed_edges if node.get_label() in [edge.get_node_1(), edge.get_node_2()] ]
        # zwroc liste tych wierzcholkow, ktore tworza krawedzie z node
        nodes_1 = {edge.get_detailed_node_1(): edge.get_travel_time() for edge in edges_with_node if node == edge.get_detailed_node_2()}
        nodes_2 = {edge.get_detailed_node_2(): edge.get_travel_time() for edge in edges_with_node if node == edge.get_detailed_node_1()}
        return dict(list(nodes_1.items()) + list(nodes_2.items()))

    def find_edge_from_nodes(self, node_1, node_2):
        for edge in self.__detailed_edges:
            if (edge.get_detailed_node_1() == node_1 and edge.get_detailed_node_2() == node_2) or (edge.get_detailed_node_2() == node_1 and edge.get_detailed_node_1() == node_2):
                return edge