"""

@author: HG
"""

"""
from backend.classes.DetailedNode import DetailedNode
from backend.classes.DetailedEdge import DetailedEdge
"""
from KMHJ.backend.classes.DetailedNode import DetailedNode
from KMHJ.backend.classes.DetailedEdge import DetailedEdge

#from backend.classes.DetailedNode import DetailedNode
#from backend.classes.DetailedEdge import DetailedEdge
import matplotlib.pyplot as plt

plt.style.use("ggplot")


class Graph:

    def __init__(self, detailed_nodes, detailed_edges, worker_time, correct_edges):
        self.__detailed_nodes = detailed_nodes
        self.__detailed_edges = detailed_edges
        self.__worker_time = worker_time
        self.__correct_edges = correct_edges
        self.__start_node = None

    # uzupełnione gettery i settery

    def get_detailed_nodes(self):
        return self.__detailed_nodes

    def get_detailed_edges(self):
        return self.__detailed_edges

    def get_worker_time(self):
        return self.__worker_time

    def get_correct_edges(self):
        return self.__correct_edges

    def get_start_node(self):
        return self.__start_node

    def set_detailed_nodes(self, detailed_nodes):
        self.__detailed_nodes = detailed_nodes

    def set_detailed_edges(self, detailed_edges):
        self.__detailed_edges = detailed_edges

    def set_worker_time(self, worker_time):
        self.__worker_time = worker_time

    def set_correct_edges(self, correct_edges):
        self.__correct_edges = correct_edges

    def set_start_node(self):
        """
        Funkcja ustalająca wierzchołek początkowy algorytmu na podstawie parametru k
        :return: None
        """
        self.__start_node = self.get_starting_node_with_max_k()

    def set_correct_edges_with_conditions(self):
        """
        Funkcja, która zwraca, czy krawędzie są poprawne tj czy się nie przecinają w grafie
        :return: 0 gdy się przecinają, nic wpp i ustawia correct_edges na True
        """
        res = True
        for edge_1 in self.get_detailed_edges():
            for edge_2 in self.get_detailed_edges():
                #node_in_edge_2 = [edge_2.get_detailed_node_1(), edge_2.get_detailed_node_()]
                if edge_1 != edge_2:
                    print("Checking edge " + edge_1.get_detailed_node_1().get_label() + " - " + edge_1.get_detailed_node_2().get_label() + " and edge " + edge_2.get_detailed_node_2().get_label() + " - " + edge_2.get_detailed_node_1().get_label())
                    res = self.check_incorrect_edges(edge_1, edge_2)
                    if res == True:
                        print("Przecinają się krawędzie")
                        self.set_correct_edges(False)
                        return 0
                    print("res = " + str(res))
        self.set_correct_edges(True)

    def check_incorrect_edges(self, edge_1, edge_2):
        """
        Funkcja, która sprawdza czy dwie krawędzie są niepoprawne w kontekście przecinania się
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
            if x1 == z1 and min(y2, v2) > max(y1, v1):
                return True
            else:
                return False
        # przypadek gdy pierwsza krawedz jest "pionowa" 
        
        if edge_1.get_detailed_node_1().get_x_coord() == edge_1.get_detailed_node_2().get_x_coord():
             if edge_2.get_detailed_node_1().get_y_coord() == edge_2.get_detailed_node_2().get_y_coord():
                 a2=0
                 b2 = edge_2.get_detailed_node_1().get_y_coord()
             else:
                a2 = (edge_2.get_detailed_node_1().get_y_coord() - edge_2.get_detailed_node_2().get_y_coord() ) / (edge_2.get_detailed_node_1().get_x_coord() - edge_2.get_detailed_node_2().get_x_coord() )
                b2 = edge_2.get_detailed_node_1().get_y_coord() - a2* edge_2.get_detailed_node_1().get_x_coord()
            
             x = edge_1.get_detailed_node_1().get_x_coord()
             y = round(a2*x+b2, 2)


             if  y > y1 and y < y2 and x>=z1 and x<=z2 :
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
       

            if  x >= x1 and x <= x2 and y>v1 and y<v2 :
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
        
        if abs(a1-a2)<0.0001:
            if abs(b1-b2) > 0.001:
                return False
            if x1 < z1 < x2 or z1<x1<z2:
                return True
            else:
                return False
        
    #wspolrzedne punktu w ktorym sie proste przecinaja
        x = round((b2-b1)/(a1-a2) ,2)
        y = round(a2*x+b2,2)
                      
        if  x > x1 and x < x2 and y > y1 and y < y2 and x >z1 and x<z2 and y>v1 and y<v2 :
            print("Krawedzie  przecinaja sie w punkcie (",x,"," ,y,")")
            return True
        else:
            return False

    def set_nodes_from_file(self, df):
        """
        Funkcja, która z data frame powstałego z pliku wejsciowego ustawia wierzcholki grafu
        :param df: df z ktorego tworzymy wierzcholki
        :return: empty, bo ustawia odpowiednio wierzcholki
        """
        records = df.values.tolist()
        for element in records:
            node = DetailedNode(element[0], element[1], element[2], element[3])
            self.__detailed_nodes.append(node)

    def set_edges_from_file(self, df):
        """
        Funkcja, która z data frame powstałego z pliku wejsciowego ustawia krawedzie grafu
        :param df: plik z ktorego tworzymy krawedzie
        :return: chyba empty, bo ustawia odpowiednio wierzcholek
        """
        records = df.values.tolist()
        for element in records:
            print("Start edge " + str(element))
            node_1_index = self.find_detailed_node_index(element[0])
            node_2_index = self.find_detailed_node_index(element[1])
            node_1 = self.__detailed_nodes[node_1_index]
            node_2 = self.__detailed_nodes[node_2_index]
            travel_time = element[2]
            # time_param i prod_param to testów:
            edge = DetailedEdge(node_1, node_2, travel_time, 0.5, 0.5)
            self.__detailed_edges.append(edge)

    def find_detailed_node_index(self, node_label):
        """
        Funkcja, która dla danego oznaczenia wierchołka zwraca jego indeks na liście wierzcholkow grafu
        :param node_label: oznaczenie node'a
        :return: index jesli istnieje, None jeśli nie
        """
        for node in self.__detailed_nodes:
            if node.get_label() == node_label:
                return self.__detailed_nodes.index(node)
        return None

    def plot_graph(self, show):
        """
        Funkcja, która rysuje graf (bez ściezki zaznaczonej)
        :param show: Parametr logiczny opisujący czy wyświetlić rysunek
        :return: empty
        """
        print("Start plot graph")
        xs = {node.get_label(): node.get_x_coord() for node in self.__detailed_nodes}
        ys = {node.get_label(): node.get_y_coord() for node in self.__detailed_nodes}
        for node in self.__detailed_nodes:
            plt.text(xs[node.get_label()], ys[node.get_label()], str(node.get_label()) + "(" + str(node.get_entrance_products()) + ")", fontsize=12, color="black")
            plt.plot(xs[node.get_label()], ys[node.get_label()], "bo")
        for edge in self.__detailed_edges:
            plt.plot([xs[edge.get_detailed_node_1().get_label()], xs[edge.get_detailed_node_2().get_label()]],
                     [ys[edge.get_detailed_node_1().get_label()], ys[edge.get_detailed_node_2().get_label()]], 'o--', color = "blue")
            if (xs[edge.get_detailed_node_1().get_label()] == xs[edge.get_detailed_node_2().get_label()]):
                plt.text(xs[edge.get_detailed_node_1().get_label()], 0.5 * ys[edge.get_detailed_node_2().get_label()] + 0.5 * ys[edge.get_detailed_node_1().get_label()], edge.get_travel_time())
            elif (ys[edge.get_detailed_node_1().get_label()] == ys[edge.get_detailed_node_2().get_label()]):
                plt.text(0.5*xs[edge.get_detailed_node_1().get_label()] + 0.5 * xs[edge.get_detailed_node_2().get_label()], ys[edge.get_detailed_node_1().get_label()], edge.get_travel_time())
            else:
                plt.text(0.5*xs[edge.get_detailed_node_1().get_label()] + 0.5 * xs[edge.get_detailed_node_2().get_label()], 0.5*ys[edge.get_detailed_node_1().get_label()] + 0.5*ys[edge.get_detailed_node_2().get_label()], edge.get_travel_time())
        plt.grid(True)
        print("Kończę rysować graf")
        if show:
            print("Pokaż graf = true")
            plt.show()
            print("Koniec funkcji plot graph")

    def plot_graph_with_path(self, path):
        """
        Funkcja, która rysuje graf z zaznaczoną ścieżką
        :param path: ścieżka do zaznaczenia
        :return: lista nazw miast odwiedzonych na ścieżce
        """
        print("start rysowania grafu ze ścieżką")
        time = self.get_worker_time()
        xs = {node.get_label(): node.get_x_coord() for node in self.__detailed_nodes}
        ys = {node.get_label(): node.get_y_coord() for node in self.__detailed_nodes}
        self.plot_graph(False)
        print("Start path to csv")
        path_to_csv = self.get_solution_from_path(path)
        maxx = xs[max(xs.keys(), key=(lambda k: xs[k]))]/2
        maxy = ys[max(ys.keys(), key=(lambda k: ys[k]))]
        print("Start rysowania krawędzi w ścieżce")
        for edge in path:
            # print("start plotting edge " + edge)
            plt.plot([xs[edge.get_detailed_node_1().get_label()], xs[edge.get_detailed_node_2().get_label()]],
                     [ys[edge.get_detailed_node_1().get_label()], ys[edge.get_detailed_node_2().get_label()]], 'ro-', label =str(edge.get_travel_time()))
            if (xs[edge.get_detailed_node_1().get_label()] == xs[edge.get_detailed_node_2().get_label()]):
                plt.text(xs[edge.get_detailed_node_1().get_label()],
                         0.5 * ys[edge.get_detailed_node_2().get_label()] + 0.5 * ys[
                             edge.get_detailed_node_1().get_label()], edge.get_travel_time())
            elif (ys[edge.get_detailed_node_1().get_label()] == ys[edge.get_detailed_node_2().get_label()]):
                plt.text(
                    0.5 * xs[edge.get_detailed_node_1().get_label()] + 0.5 * xs[edge.get_detailed_node_2().get_label()],
                    ys[edge.get_detailed_node_1().get_label()], edge.get_travel_time())
            else:
                plt.text(
                    0.5 * xs[edge.get_detailed_node_1().get_label()] + 0.5 * xs[edge.get_detailed_node_2().get_label()],
                    0.5 * ys[edge.get_detailed_node_1().get_label()] + 0.5 * ys[edge.get_detailed_node_2().get_label()],
                    edge.get_travel_time())
        plt.text(maxx, maxy, ("Dla czasu: " + str(time)), size=10, color='purple')
        print("Napisałem dla czasu")
        plt.show()
        print("Kończy działanie plot graph with path")
        return path_to_csv

    def get_solution_from_path(self, path):
        """
        Funkcja, która zwraca listę nazw wierzchołków na podstawie listy DetailedEdge
        :param path: lista DetaileEdge, z której chcemy wyekstartować wierzchołki
        :return: lista nazw wierzchołków z path w kojeności przejścia
        """
        path_to_csv = []
        path_tmp = []
        for edge in path:
            path_tmp.append(edge)

        # last_node = self.get_starting_node()
        print("Ustalam last node")
        last_node = self.get_start_node()
        print("last node to " + last_node.get_label())
        path_to_csv.append(last_node.get_label())
        print("W path_tmp zostało: ")
        for edget in path_tmp:
            print(edget.get_detailed_node_1().get_label() + "->" + edget.get_detailed_node_2().get_label())

        while path_tmp:
            print("Jestem w petli path_tmp")
            len_path_tmp = len(path_tmp)
            for edge in path_tmp:
                if edge.get_detailed_node_1() == last_node:
                    print("Dodaje krawedz " + edge.get_detailed_node_1().get_label() + "->" + edge.get_detailed_node_2().get_label())
                    path_to_csv.append(edge.get_detailed_node_2().get_label())
                    path_tmp.remove(edge)
                    last_node = edge.get_detailed_node_2()
                    break
                elif edge.get_detailed_node_2() == last_node:
                    print("Dodaje krawedz " + edge.get_detailed_node_1().get_label() + "->" + edge.get_detailed_node_2().get_label())
                    print("W path_tmp zostało: " + str(len(path_tmp)))
                    path_to_csv.append(edge.get_detailed_node_1().get_label())
                    path_tmp.remove(edge)
                    last_node = edge.get_detailed_node_1()
                    break
            if len(path_tmp) == len_path_tmp:
                print("Nie można wyznaczyć rozwiązania")
                path_to_csv = []
                break

        return path_to_csv

    def get_nodes_from_path(self, path, start_node):
        """
        Funkcja, która zwraca listę DetailedNode na podstawie listy DetailedEdge i pierwszego wierzchołka ścieżki
        :param path: lista DetaileEdge, z której chcemy wyekstartować wierzchołki
        :param start_node: wierzchołek, od ktorego scieżka się zaczyna
        :return: lista DetailedNode
        """
        nodes = []
        path_tmp = []
        for edge in path:
            path_tmp.append(edge)
        # last_node = self.get_starting_node()
        print("Ustalam last node")
        last_node = start_node
        print("last node to " + last_node.get_label())
        nodes.append(last_node)
        print("W path_tmp zostało: ")
        for edget in path_tmp:
            print(edget.get_detailed_node_1().get_label() + "->" + edget.get_detailed_node_2().get_label())

        while path_tmp:
            print("Jestem w petli path_tmp")
            len_path_tmp = len(path_tmp)
            for edge in path_tmp:
                if edge.get_detailed_node_1() == last_node:
                    print("Dodaje krawedz " + edge.get_detailed_node_1().get_label() + "->" + edge.get_detailed_node_2().get_label())
                    nodes.append(edge.get_detailed_node_2())
                    path_tmp.remove(edge)
                    last_node = edge.get_detailed_node_2()
                    break
                elif edge.get_detailed_node_2() == last_node:
                    print("Dodaje krawedz " + edge.get_detailed_node_1().get_label() + "->" + edge.get_detailed_node_2().get_label())
                    print("W path_tmp zostało: " + str(len(path_tmp)))
                    nodes.append(edge.get_detailed_node_1())
                    path_tmp.remove(edge)
                    last_node = edge.get_detailed_node_1()
                    break
            if len(path_tmp) == len_path_tmp:
                print("Nie można wyznaczyć wierzchołków")
                nodes = []
                break
        return nodes

    def get_neighbours(self, node):
        """
        Funkcja która zwraca sąsiadów wierzchołka node i wagi do sąsiadów ze wzoru liczonego dla algorytmu
        :param node: node, którego sąsiadów szukamy
        :return: słownik sąsiedzi: wagi
        """
        if node is None:
            return dict()
        # zwrot te krawedzie, ktore zawieraja node w sobie
        edges_with_node = [edge for edge in self.__detailed_edges if node.get_label() in [edge.get_detailed_node_1().get_label(), edge.get_detailed_node_2().get_label()]]
        # zwroc liste tych wierzcholkow, ktore tworza krawedzie z node
        nodes_1 = {edge.get_detailed_node_1(): edge.get_weight_to_1() for edge in edges_with_node if node == edge.get_detailed_node_2()}
        nodes_2 = {edge.get_detailed_node_2(): edge.get_weight_to_2() for edge in edges_with_node if node == edge.get_detailed_node_1()}
        return dict(list(nodes_1.items()) + list(nodes_2.items()))

    def get_edges_from_node(self, node):
        """
        Funkcja zwracająca wszytstkie krawędzie zawierajace wskazany wierzchołek.
        :param node: wierzcholek na podstawie którego chcemy znaleźć krawędzie
        :return: lista krawędzi zawierajacych wskazany wierzchołek
        """
        edges_to_node = [edge for edge in self.__detailed_edges if node.get_label() == edge.get_detailed_node_2().get_label() or node.get_label() == edge.get_detailed_node_1().get_label()]
        print("Krawędzi wierzchołka " + node.get_label() + " jest " + str(len(edges_to_node)))
        return edges_to_node

    def find_edge_from_nodes(self, node_1, node_2):
        """
        Funkcja znajdująca w grafie krawędź na podstawie wierzchołków
        :param node_1: Wierzchołek z klasy Detailed Node
        :param node_2: Wierzchołek z klasy Detailed Node
        :return: Krawędź node_1 -- node_2 gdy istnieje, empty wpp
        """
        for edge in self.__detailed_edges:
            if (edge.get_detailed_node_1() == node_1 and edge.get_detailed_node_2() == node_2) or (edge.get_detailed_node_2() == node_1 and edge.get_detailed_node_1() == node_2):
                return edge

        """
        funkcja wyznaczajaca wspolczynnik k
        oraz wfunkcja wyznaczajaca wierzcholek z najwiekszym wspolczynnikiem k
        """
     
    def get_starting_node_with_max_k(self):
        """
        :return: zwraca wierzchołek z największym parametrem k

        """
        # node = DetailedNode("Zero", 1, 1, 0)
        node_max = max([node.get_k_value_to_node(self) for node in self.__detailed_nodes])
        node = [x for x in self.__detailed_nodes if x.get_k_value_to_node(self) == node_max]
        #for n in self.__detailed_nodes:
        #    if node.get_k_value_to_node(self) < n.get_k_value_to_node(self):
        #        node = n
        print("Dlugosc list node to ", str(len(node)))
        return node[0]

    def get_node_from_label(self, label):
        """
        Funkcja, która zwraca wierzchołek na podstawie labelki
        :param label: oznaczenie wierzchołka
        :return: Wierzchołek, gdy jego label == argument, None wpp
        """
        for node in self.__detailed_nodes:
            if node.get_label() == label:
                return node
        return None

    def read_solution_from_file(self, df):
        records = df.values.tolist()
        solution_path = []
        for element in records:
            node_label = element[0]
            node = self.get_node_from_label(node_label)
            solution_path.append(node)
        return solution_path
    """
    
    SPÓJNOSC
    """
    def DFS(self, v, visited):
        """
            funkcja przeszukuje graf w glab i zaznacza ktore wierzcholki zostaly odwiedzone
            :param v: obecnie sprawdzany wierzchołek
            :param visited: tablica tablic mowiaca ktore wierzcholki zostaly juz odwiedzone
        """
       
        # mark current node as visited
        for x in visited :
            if x[1]==v.get_label() :
                x[0]=True
                # print(visited)
                break
        # print("odwiedzilem: " + v.get_label())
        # do for every edge `v —> u`
        # print("sasiedzi "+ v.get_label() + str(self.get_neighbours(v)))
        for u in self.get_neighbours(v):
            # `u` is not visited
            for x in visited:
                if u.get_label()==x[1] and not x[0]:
                    self.DFS(u, visited)
 
 
# Check if the graph is strongly connected or not
    def check(self):
        """
        :return: zwraca True jesli graf jest spojny
                wpp zwraca False
        """
    # do for every vertex
        # print("wierzcholki mi wyswietl " + self.get_detailed_nodes())
        for i in self.get_detailed_nodes():
            # to keep track of whether a vertex is visited or not
            visited = [[False, x.get_label()] for x in self.get_detailed_nodes()]
            # print(visited)
            # start DFS from the first vertex
            self.DFS(i, visited) 
            # If DFS traversal doesn't visit all vertices,
            # then the graph is not strongly connected
            for b in visited:
                if not b[0]:
                    return False 
        return True
