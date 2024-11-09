
class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []
        self.path = []


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


my_graph = Graph()
green_lake = Node("Green Lake")
uw = Node("UW")
cap_hill = Node("Capitol Hill")
slu = Node("South Lake Union")
fremont = Node("Fremont")
space_needle = Node("Space Needle")

my_graph.insertNode(green_lake)
my_graph.insertNode(uw)
my_graph.insertNode(cap_hill)
my_graph.insertNode(slu)
my_graph.insertNode(fremont)
my_graph.insertNode(space_needle)

my_graph.addEdge(green_lake, uw)
my_graph.addEdge(green_lake, slu)
my_graph.addEdge(uw, cap_hill)
my_graph.addEdge(cap_hill, slu)
my_graph.addEdge(slu, fremont)
my_graph.addEdge(fremont, green_lake)
my_graph.addEdge(fremont, space_needle)

my_graph.breadthFirstSearch(green_lake, space_needle)


print('\n\n\n')

print(my_graph.nodes)