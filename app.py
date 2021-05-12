from GUI.files import GUI, Error, Save
from backend.MathFuncs.MathFunctions import solve_salesman_problem
from backend.classes.Graph import Graph
import pandas as pd

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
            if not graph.get_correct_edges():
                print("Warunek nieprzecinania niespełniony!")
                Error("Co najmniej dwie z podanych dróg przecinają się.")
                continue
            #TODO tutaj dodać czy graf jest spojny zweryfikowanie @Kto?
            graph.plot_graph(True)
        except Exception as ex:
            print("Nie udało się utworzyć grafu.")
            Error("Nie udało sie utworzyć grafu. ")
            print(ex)
            continue
        if len(list_of_dfs) == 3:
            try:
                graph.set_correct_edges_with_conditions()
                solved = solve_salesman_problem(graph)
                result = graph.plot_graph_with_path(solved)
                result = pd.DataFrame(result, columns=['solution'])
            except:
                print("Nie udało się rozwiązać problemu")
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
                for i in range(len(solution_data_list_tmp)-1):
                    solution_data_list.append(graph.find_edge_from_nodes(graph.get_node_from_label(solution_data_list_tmp[i]), graph.get_node_from_label(solution_data_list_tmp[i+1])))
                solution_data = [solution_data_list, solution_data_list[-1]]
            except:
                print("Nie udało się przeczytać rozwiązania.")
                Error("Nie udało się przeczytać rozwiązania.")
                continue
            try:
                result = graph.plot_graph_with_path(solution_data)
            except Exception as ex:
                print("Nie udało się wyświetlić grafu z rozwiązaniem because of ")
                print(ex)
                Error("Nie udało sie wyświetlić grafu. ")
