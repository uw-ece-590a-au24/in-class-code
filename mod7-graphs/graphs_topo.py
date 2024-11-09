
class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []
        self.path = []
        self.in_degree = 0


    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def __repr__(self):
        return self.data + str(self.neighbors)

class Graph:
    def __init__(self):
        self.nodes = []
        # self.node_list = {} ## Dictionary, with Key = source, Value = List of neighbors

    def insertNode(self, node):
        self.nodes.append(node)
        ## COULD: Put the node with an empty list into the dictionary
        # self.node_list[node] = []

    def addEdge(self, source:Node, destination:Node):
        ## Assume source & destination are in teh list of nodes
        source.addNeighbor(destination)

        ## IF we were using a dictionary.
        # self.nodes[source].append(destination)

        pass

    def breadthFirstSearch(self, source:Node, destination:Node):
        nodes_to_visit = [source]
        for node in self.nodes:
            node.path = []

        while len(nodes_to_visit) > 0:
            cur_node = nodes_to_visit.pop(0)
            print("We're at node: " + cur_node.data, end = " ")
            print(cur_node.path)

            if cur_node == destination:
                print("We're at the destination!")
                return

            for i in cur_node.neighbors:
                ## Trying to store the path to each node, so we know how we got there.
                i.path = cur_node.path
                i.path.append(cur_node.data)
                nodes_to_visit.append(i)

        print("No path exists between source and destination")

        pass

    def topologicalSort(self):
        # in_degree = [] ## Each entry in_degree[i] = in_degree of self.nodes[i]
        output_order = []

        ## initialize in_degree
        for index, node in enumerate(self.nodes):
            for neighbor in node.neighbors:
                neighbor.in_degree += 1

        nodes_to_visit = [] ## List of indexes of nodes that have in_degree = 0
        for node in self.nodes:
            if node.in_degree == 0:
                nodes_to_visit.append(node)

        while len(nodes_to_visit) > 0:
            cur_node = nodes_to_visit.pop()
            output_order.append(cur_node.data)
            for neighbor in cur_node.neighbors:

                neighbor.in_degree -= 1
                if neighbor.in_degree == 0:
                    nodes_to_visit.append(neighbor)

        return output_order






my_graph = Graph()
node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")
node_g = Node("G")

my_graph.insertNode(node_a)
my_graph.insertNode(node_b)
my_graph.insertNode(node_c)
my_graph.insertNode(node_d)
my_graph.insertNode(node_e)
my_graph.insertNode(node_f)
my_graph.insertNode(node_g)

my_graph.addEdge(node_g, node_a)
my_graph.addEdge(node_g, node_f)
my_graph.addEdge(node_a, node_c)
my_graph.addEdge(node_a, node_b)
my_graph.addEdge(node_b, node_d)
my_graph.addEdge(node_b, node_c)
my_graph.addEdge(node_c, node_f)
my_graph.addEdge(node_f, node_e)
my_graph.addEdge(node_c, node_e)
my_graph.addEdge(node_e, node_d)

output = my_graph.topologicalSort()

print(output)