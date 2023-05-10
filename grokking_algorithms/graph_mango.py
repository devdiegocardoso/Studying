# pylint: disable=missing-docstring

from collections import deque
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    profession: str

    def hash_value(self):
        return self.name
    def is_mango_seller(self):
        return self.profession == "mango seller"

alice = Person("alice","teacher")
bob = Person("bob","singer")
claire = Person("claire","actress")
anuj = Person("anuj","astronaut")
peggy = Person("peggy","lawyer")
thom = Person("thom","mango seller")
jonny = Person("jonny","programmer")

graph = {
    "you": [alice, bob, claire],
    "bob": [anuj, peggy],
    "alice": [peggy],
    "claire": [thom, jonny],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": [],
}

def bfs(queue):
    checked = []
    while queue:
        current_person = queue.popleft()
        if current_person not in checked:
            if current_person.is_mango_seller():
                print(f"{current_person.name} sells mango!")
                return True
            queue += graph[current_person.hash_value()]
            checked.append(current_person)
    print("Nobody sells mango :(")
    return False

search_queue = deque()
search_queue += graph["you"]

bfs(search_queue)
