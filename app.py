from GUI.files import GUI, Error, Save
from KMHJ.backend.MathFuncs.MathFunctions import solve_salesman_problem
from KMHJ.backend.classes.Graph import Graph
import pandas as pd
from func_timeout import func_timeout, FunctionTimedOut
import time


TIMEOUT_PARAM = 30

if __name__ == "__main__":

    while True:
        try:
            list_of_dfs = GUI()
        except:
            print("Koniec przetworzenia GUI")
            break

        try:
            graph = Graph([], [], None, None)
            graph.set_nodes_from_file(list_of_dfs[0])
            for node in graph.get_detailed_nodes():
                print(node.get_label())
            graph.set_edges_from_file(list_of_dfs[1])
            graph.set_worker_time(list_of_dfs[2].values.tolist()[0][0])
            graph.set_correct_edges_with_conditions()
            graph.set_start_node()

            if not graph.check():
                print("Graf nie jest spojny!!!")
                Error("Graf nie jest spojny!!!")
                continue               
            if not graph.get_correct_edges():
                print("Warunek nieprzecinania niespełniony!")
                Error("Co najmniej dwie z podanych dróg przecinają się.")
                continue
            #TODO tutaj dodać czy graf jest spojny zweryfikowanie @Kto?
        except Exception as ex:
            print(ex)
            print("Nie mogę utworzyć grafu.")

        if len(list_of_dfs) == 3:
            try:
                graph.plot_graph(True)
            except Exception as ex:
                print(ex)
                print("Nie mogę wyświetlić grafu bez ścieżki.")
            try:
                path_arg = []
                start_time = time.time()
                [path, time_left, prod_sold] = func_timeout(TIMEOUT_PARAM, solve_salesman_problem, args=(graph, path_arg))
                print("----------- Znalazłem rozwiązanie w: " + str(time.time()-start_time) + " sekund --------------")
            except FunctionTimedOut:
                print("Mineło " + str(TIMEOUT_PARAM) + " sekund - zwracam rozwiązanie przybliżone")
                path = path_arg.copy()
                [time_left, prod_sold] = graph.calculate_result(path)
            except Exception as ex:
                print(ex)
                print("Nie mogłem utworzyć rozwiązania")
            try:
                print("Wypisuję krawędzie w ścieżce: ")
                for edge in path:
                    print(edge.get_detailed_node_1().get_label() + "->" + edge.get_detailed_node_2().get_label())
                print("Scieżka została przebyta w czasie " + str(graph.get_worker_time() - time_left) + " podczas, której sprzedano " + str(prod_sold) + " towarów")
                result = graph.plot_graph_with_path(path, time_left, prod_sold)
                Error("Czas sprzedawcy: " + str(graph.get_worker_time()) + "\nScieżka została przebyta w czasie: " + str(graph.get_worker_time() - time_left) + "\nSprzedanych towarów: " + str(prod_sold))
                result = pd.DataFrame(result, columns=['solution'])
            except Exception as ex:
                print("Nie udało się rozwiązać problemu")
                print(ex)
                Error("Nie udało się rozwiązać problemu.")
                continue
            try:
                Save(result)
                continue
            except:
                print("Nie udało się zapisać pliku z rozwiązaniem.")
                Error("Nie udało się zapisać pliku z rozwiązaniem.")

        elif len(list_of_dfs) == 4:  # co oznacza że wczytano wszystkie pliki i już niech bangla wczytane rozwiązanie
            try:
                solution_data_list_tmp = graph.read_solution_from_file(list_of_dfs[3])
                solution_data_list = list()
                print(solution_data_list_tmp)
                for i in range(len(solution_data_list_tmp)-1):
                    solution_data_list.append(graph.find_edge_from_nodes(solution_data_list_tmp[i], solution_data_list_tmp[i+1]))
            except Exception as ex:
                print("Nie udało się przeczytać rozwiązania.")
                Error("Nie udało się przeczytać rozwiązania.")
                print(ex)
                continue
            try:
                result = graph.plot_graph_with_path(solution_data_list)
            except Exception as ex:
                print("Nie udało się wyświetlić grafu z rozwiązaniem ponieważ")
                print(ex)
                Error("Nie udało sie wyświetlić grafu.")
