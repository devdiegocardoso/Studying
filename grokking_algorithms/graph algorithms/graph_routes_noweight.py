# pylint: disable=missing-docstring

from collections import deque, defaultdict
from dataclasses import dataclass

@dataclass
class Place:
    name: str

    def hash_value(self):
        return self.name

    def is_my_goal(self, goal):
        return self.name == goal

twin_peaks = Place("twin peaks")
point_a = Place("A")
point_b = Place("B")
point_c = Place("C")
point_d = Place("D")
point_e = Place("E")
golden_gate = Place("golden gate")

graph = {
    "twin peaks": [point_a, point_b],
    "A": [point_d],
    "B": [point_c, point_e],
    "C": [point_d],
    "D": [golden_gate],
    "E": [point_d],
    "golden gate": [],
}

def print_route(end, parents_list):
    print("Route found!")
    route = [end.hash_value()]
    current_node = parents_list[end.hash_value()][0]
    create_route(parents_list, route, current_node)
    print(route)

def create_route(parents_list, route, current_node):
    while current_node:
        route.append(current_node[0])
        current_node = parents_list[current_node[0]]
    route.reverse()

def create_parents_list(parents_list, current_parent):
    for child in graph[current_parent.hash_value()]:
        parents_list.setdefault(child.hash_value(), []).append(current_parent.hash_value())

def bfs(queue):
    checked = []
    while queue:
        current_place = queue.popleft()
        if current_place not in checked:
            if current_place.is_my_goal("golden gate"):
                print_route(current_place, parents)
                return True
            process_node(queue, checked, current_place)
    print("No route found :(")
    return False

def process_node(queue, checked, current_place):
    queue.extend(graph[current_place.hash_value()])
    checked.append(current_place)
    create_parents_list(parents, current_place)

search_queue = deque()
search_queue.extend(graph[twin_peaks.hash_value()])
parents = defaultdict(list)
create_parents_list(parents, twin_peaks)

bfs(search_queue)
