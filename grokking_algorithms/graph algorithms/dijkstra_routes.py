# pylint: disable=missing-docstring

GOAL = "finish"
INFINITY = float("inf")

graph = {
    "start": {"a":6,"b":2},
    "a": {"finish":1},
    "b": {"a":3,"finish":5},
    "finish": {},
}

costs = {
    "a":6,
    "b":2,
    "finish": INFINITY
}

parents = {
    "start": None,
    "a":"start",
    "b":"start",
    "finish": None
}

processed = []

def find_lowest_cost_node():
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node,cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def dijkstra():
    current_node = find_lowest_cost_node()
    while current_node is not None:
        cost = costs[current_node]
        neighbors = graph[current_node]
        for node in neighbors.keys():
            new_cost = cost + neighbors[node]
            if costs[node] > new_cost:
                costs[node] = new_cost
                parents[node] = current_node
        processed.append(current_node)
        current_node = find_lowest_cost_node()

dijkstra()

track_node = parents[GOAL]
route = [GOAL]
while track_node:
    route.append(track_node)
    track_node = parents[track_node]

route.reverse()
print(f"Route: {route}")
print(f"Minimum time: {costs[GOAL]}")
