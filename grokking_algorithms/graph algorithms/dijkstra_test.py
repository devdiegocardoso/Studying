# pylint: disable=missing-docstring

import unittest
from dijkstra import Dijkstra, BFS
from node import Node

INFINITY = float("inf")

class TestGraphSearch(unittest.TestCase):
    def setUp(self):
        self.graph = BFS()
        self.twin_peaks = Node("twin peaks")
        self.point_a = Node("A")
        self.point_b = Node("B")
        self.point_c = Node("C")
        self.point_d = Node("D")
        self.point_e = Node("E")
        self.golden_gate = Node("golden gate")
        self.fill_graph()

    def fill_graph(self):
        self.graph.add_node(self.twin_peaks,self.point_a)
        self.graph.add_node(self.twin_peaks,self.point_b)
        self.graph.add_node(self.point_a,self.point_d)
        self.graph.add_node(self.point_b,self.point_c)
        self.graph.add_node(self.point_b,self.point_e)
        self.graph.add_node(self.point_c,self.point_d)
        self.graph.add_node(self.point_d,self.golden_gate)
        self.graph.add_node(self.point_e,self.point_d)
        self.graph.add_node(self.golden_gate)

        self.graph.start_from(self.twin_peaks)
    def test_bfs_found(self):
        self.assertTrue(self.graph.bfs("golden gate"))
    def test_bfs_not_found(self):
        self.assertFalse(self.graph.bfs("silver gate"))
    def test_bfs_generated_route(self):
        self.graph.bfs("golden gate")
        self.assertListEqual(self.graph.get_route(),["twin peaks", "A", "D", "golden gate"])

class TestDijkstraSearch(unittest.TestCase):
    def setUp(self):
        self.graph = Dijkstra()
        self.twin_peaks = Node("twin peaks")
        self.point_a = Node("A")
        self.point_b = Node("B")
        self.golden_gate = Node("golden gate")
        self.fill_graph()

    def fill_graph(self):
        self.graph.add_node(self.twin_peaks,self.point_a,6)
        self.graph.add_node(self.twin_peaks,self.point_b,2)
        self.graph.add_node(self.point_a,self.golden_gate,1)
        self.graph.add_node(self.point_b,self.point_a,3)
        self.graph.add_node(self.point_b,self.golden_gate,5)
        self.graph.add_node(self.golden_gate)

        self.graph.set_cost(self.point_a,6)
        self.graph.set_cost(self.point_b,2)
        self.graph.set_cost(self.golden_gate,INFINITY)

        self.graph.set_parent(self.twin_peaks)
        self.graph.set_parent(self.point_a,self.twin_peaks)
        self.graph.set_parent(self.point_b,self.twin_peaks)
        self.graph.set_parent(self.golden_gate)

    def test_dijkstra_route(self):
        self.graph.dijkstra(self.golden_gate)
        self.assertListEqual(self.graph.get_route(),[self.twin_peaks, self.point_b, self.point_a, self.golden_gate])
    def test_dijkstra_cost(self):
        cost = self.graph.dijkstra(self.golden_gate)
        self.assertEqual(cost,6)

if __name__ == '__main__':
    unittest.main()
