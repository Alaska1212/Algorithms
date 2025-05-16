"""
Нехай задано орієнтований зважений граф.
Знайдіть довжину найкоротшого шляху між двома заданими вузлами цього графа
"""
import sys

INF = sys.maxsize

graph : list
def init(vertices, edges):
    """ Ініціалізація графа.

    Викликається один раз на початку виконання програми.
    @param vertices: кількість вершин графа
    @param edges:  кількість ребер графа
    """
    global graph
    graph = [{} for _ in range(vertices)]


def addEdge(source, destination, weight):
    """ Додає зважене ребро графа

    @param source: вершини з якої виходить ребро
    @param destination: вершина у яку входить ребро
    @param weight: вага ребра
    """
    graph[source][destination] = weight


def findDistance(start, end):
    """ Знаходить довжину найкоротшого шляху, між двома заданими вершинами графа

    @param start: початкова вершина
    @param end: кінцева вершина
    @return: Довжину найкоротшого шляху або -1 якщо шляху між вершинами не існує.
    """
    vertices = len(graph)
    distance = [INF] * vertices
    distance[start] = 0

    for _ in range(vertices - 1):
        for u in range(vertices):
            for v, w in graph[u].items():
                if distance[u] != INF and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

    for u in range(vertices):
        for v, w in graph[u].items():
            if distance[u] != INF and distance[u] + w < distance[v]:
                return -1

    return distance[end] if distance[end] != INF else -1

if __name__ == "_main__":
    init(6,0)
    addEdge(0,1,8)
    addEdge(0, 2, 7)
    addEdge(0, 3, 2)
    addEdge(0, 4, 1)
    addEdge(1, 4, 2)
    addEdge(1, 5, 5)