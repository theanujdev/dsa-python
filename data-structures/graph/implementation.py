class Graph():
    def __init__(self) -> None:
        self.number_of_nodes = 0
        self.adjacency_list = {}

    def insert_node(self, data):
        if data not in self.adjacency_list:
            self.adjacency_list[data] = []
            self.number_of_nodes += 1

    def insert_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def show_connections(self):
        for node in self.adjacency_list:
            print(
                f'{node} -->> {" ".join(map(str, self.adjacency_list[node]))}')


#     2 ---- 0
#   /   \
#  1     3

# Edge List
# graph = [[0, 2], [2, 3], [2, 1], [1, 3]]

# Adjacent List
# graph = [[2], [2, 3], [0, 1, 3], [1, 2]]

# Adjacent Matrix (with weight)
# graph = {
#     0: [0, 0, 1, 0],
#     1: [0, 0, 1, 1],
#     2: [1, 1, 0, 1],
#     3: [0, 1, 1, 0]
# }

my_graph = Graph()
my_graph.insert_node(1)
my_graph.insert_node(2)
my_graph.insert_node(3)
my_graph.insert_edge(1, 2)
my_graph.insert_edge(1, 3)
my_graph.insert_edge(2, 3)
my_graph.show_connections()
