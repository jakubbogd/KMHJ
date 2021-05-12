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
            #TODO Tutaj potrzeba funkcji która wypisze użytkownikowi, że się zjebawsy @Kubuś - proszę
                continue
            #TODO tutaj dodać czy graf jest spojny zweryfikowanie @Kto?
            graph.plot_graph(True)
        except Exception as ex:
            print("Nie udało się utworzyć grafu.")
            Error("Nie udało sie utworzyć grafu. "+str(ex.getMessage()))
            #TODO Okienko że nie udało się utworzyć grafu + ex.getMessage()? @Kuba - czy tak?
            continue
        if len(list_of_dfs) == 3:
            try:
                graph.set_correct_edges_with_conditions()
                solved = solve_salesman_problem(graph)
                result = graph.plot_graph_with_path(solved)
                result = pd.DataFrame(result, columns=['Miasta'])
            except:
                print("Nie udało się rozwiązać problemu")
                Error("Nie udało się rozwiązać problemu.")
                #TODO okienko że nie udało się rozwiązać problemu - proszę
                # muszę obsłużyć jeszcze żeby rozwiązywało się maks ileś czasu ale na betę chyba nie trzeba @Hubi
                continue
            try:
                #TODO okienko dla użytkownika, żeby podał gdzie chce zapisać plik @Kubuś i tam zapisać - proszę
                Save(result)
                continue
                # TODO wyskakuje dla uztywkonika że zapisano rozwiązanie i gdy zamknie, to wyskakuje mu na nowo wszystko od nowa @Kubuś
            except:
                print("Nie udało się zapisać pliku z rozwiązaniem.")
                Error("Nie udało się zapisać pliku z rozwiązaniem.")
                #TODO okienko dla użytkownika, że nie udało się zapisać pliku z rozwiązaniem @Kubuś - proszę

        elif len(list_of_dfs) == 4:  # co oznacza że wczytano wszystkie pliki i już niech bangla wczytane rozwiązanie
            try:
                solution_data_list = graph.read_solution_from_file(list_of_dfs[3])
                solution_data = [solution_data_list, solution_data_list[-1]]
            except:
                print("Nie udało się przeczytać rozwiązania.")
                Error("Nie udało się przeczytać rozwiązania.")
                # TODO wyskakuje dla uztywkonika że nie udalo sie przeczytac rozwiaznia i gdy zamknie, to wyskakuje mu na nowo wszystko od nowa @Kubuś
                continue
            try:
                result = graph.plot_graph_with_path(solution_data)
            except Exception as ex:
                print("Nie udało się wyświetlić grafu z rozwiązaniem because of ")
                print(ex)
                Error("Nie udało sie wyświetlić grafu. "+str(ex.getMessage()))
                # TODO Okienko dla usera z komunikatem - proszę
