# pylint: disable=missing-docstring

from collections import deque
from node import Node

class Graph():
    def __init__(self) -> None:
        self.graph = {}
        self.parent_dict = {}
        self.search_queue = deque()
        self.checked = []
        self.route = []

    def get_route(self):
        return self.route

    def start_from(self,node: Node):
        self.search_queue.append(node)

    def add_node(self, parent:Node, child:Node=None):
        self.graph.setdefault(parent,[])
        if child:
            self.graph[parent].append(child)

    def create_route(self,current_node):
        while current_node:
            self.route.append(current_node.name)
            current_node = self.parent_dict.get(current_node,None)
        self.route.reverse()

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
