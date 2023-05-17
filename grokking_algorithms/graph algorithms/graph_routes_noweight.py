# pylint: disable=missing-docstring

from collections import deque, defaultdict
from dataclasses import dataclass

@dataclass
class Place:
    _name: str

    def __hash__(self):
        return hash(self._name)

    def __eq__(self, __value: object) -> bool:
        return __value == self._name if isinstance(__value,Place) else False
    
    def __repr__(self) -> str:
        return self._name

    def is_my_goal(self, goal):
        return self._name == goal

    @property
    def name(self):
        return self._name

twin_peaks = Place("twin peaks")
point_a = Place("A")
point_b = Place("B")
point_c = Place("C")
point_d = Place("D")
point_e = Place("E")
golden_gate = Place("golden gate")

graph = {
    twin_peaks: [point_a, point_b],
    point_a: [point_d],
    point_b: [point_c, point_e],
    point_c: [point_d],
    point_d: [golden_gate],
    point_e: [point_d],
    golden_gate: [],
}

def print_route(end, parents_list):
    print("Route found!")
    route = [end]
    current_node = parents_list[end][0]
    create_route(parents_list, route, current_node)
    print(route)

def create_route(parents_list, route, current_node):
    while current_node:
        route.append(current_node)
        current_node = parents_list[current_node][0] if parents_list[current_node] else None
    route.reverse()

def create_parents_list(parents_list, current_parent):
    for child in graph[current_parent]:
        parents_list.setdefault(child, []).append(current_parent)

def bfs(queue,goal):
    checked = []
    while queue:
        current_place = queue.popleft()
        if current_place not in checked:
            if current_place.is_my_goal(goal):
                print_route(current_place, parents)
                return True
            process_node(queue, checked, current_place)
    print("No route found :(")
    return False

def process_node(queue, checked, current_place):
    queue.extend(graph[current_place])
    checked.append(current_place)
    create_parents_list(parents, current_place)

search_queue = deque()
search_queue.extend(graph[twin_peaks])
parents = defaultdict(list)
create_parents_list(parents, twin_peaks)

bfs(search_queue,"golden gate")
