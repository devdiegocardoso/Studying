# pylint: disable=missing-docstring

from collections import deque
from node import Node

class Graph():
    def __init__(self) -> None:
        self.graph = {}
        self.parent_dict = {}
        self.checked = []
        self.route = []

    def get_route(self):
        return self.route

    def add_node(self, parent:Node, child:Node=None,cost=0):
        self.graph.setdefault(parent,{})
        if child:
            self.graph[parent].update({child:cost})

    def set_parent(self,child:Node,parent:Node=None):
        self.parent_dict[child] = parent


class Dijkstra(Graph):
    def __init__(self) -> None:
        Graph.__init__(self)
        self.costs = {}

    def set_cost(self,node:Node,cost=0):
        self.costs[node] = cost

    def find_lowest_cost_node(self):
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node,cost in self.costs.items():
            if cost < lowest_cost and node not in self.checked:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    def dijkstra(self,goal:Node):
        current_node = self.find_lowest_cost_node()
        while current_node is not None:
            current_node = self.pick_new_node(current_node)

        self.find_route(goal)
        return self.costs[goal]

    def pick_new_node(self, current_node):
        cost = self.costs[current_node]
        neighbors = self.graph[current_node]
        for node in neighbors.keys():
            self.evaluate_cost(current_node, cost, neighbors, node)
        self.checked.append(current_node)
        return self.find_lowest_cost_node()

    def evaluate_cost(self, current_node, cost, neighbors, node):
        new_cost = cost + neighbors[node]
        if self.costs[node] > new_cost:
            self.costs[node] = new_cost
            self.parent_dict[node] = current_node

    def find_route(self, goal):
        track_node = self.parent_dict[goal]
        self.route.append(goal)
        while track_node:
            self.route.append(track_node)
            track_node = self.parent_dict[track_node]
        self.route.reverse()

class BFS(Graph):
    def __init__(self) -> None:
        Graph.__init__(self)
        self.search_queue = deque()

    def create_route(self,current_node):
        while current_node:
            self.route.append(current_node.name)
            current_node = self.parent_dict.get(current_node,None)
        self.route.reverse()

    def start_from(self,node: Node):
        self.search_queue.append(node)

    def bfs(self,goal):
        while self.search_queue:
            current_place = self.search_queue.popleft()
            if current_place.is_my_goal(goal):
                self.create_route(current_place)
                return True
            for child in self.graph[current_place]:
                self.process_node(current_place, child)
        return False

    def process_node(self, current_place, child):
        if child not in self.checked:
            self.search_queue.append(child)
            self.checked.append(child)
            self.parent_dict[child] = current_place
