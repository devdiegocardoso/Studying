# pylint: disable=missing-docstring

import unittest
from graph import Graph
from node import Node

class TestGraph1Search(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.fill_graph()
    def fill_graph(self):
        twin_peaks = Node("twin peaks")
        point_a = Node("A")
        point_b = Node("B")
        point_c = Node("C")
        point_d = Node("D")
        point_e = Node("E")
        golden_gate = Node("golden gate")
        self.graph.add_node(twin_peaks,point_a)
        self.graph.add_node(twin_peaks,point_b)
        self.graph.add_node(point_a,point_d)
        self.graph.add_node(point_b,point_c)
        self.graph.add_node(point_b,point_e)
        self.graph.add_node(point_c,point_d)
        self.graph.add_node(point_d,golden_gate)
        self.graph.add_node(point_e,point_d)
        self.graph.add_node(golden_gate)

        self.graph.start_from(twin_peaks)
    def test_bfs_found(self):
        self.assertEqual(self.graph.bfs("golden gate"),True)
    def test_bfs_not_found(self):
        self.assertEqual(self.graph.bfs("silver gate"),False)
    def test_bfs_generated_route(self):
        self.graph.bfs("golden gate")
        self.assertEqual(self.graph.get_route(),["twin peaks", "A", "D", "golden gate"])

class TestGraph2Search(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.fill_graph()
    def fill_graph(self):
        start = Node("start")
        point_a = Node("A")
        point_b = Node("B")
        end = Node("end")
        self.graph.add_node(start,point_a)
        self.graph.add_node(start,point_b)
        self.graph.add_node(point_a,end)
        self.graph.add_node(point_b,point_a)
        self.graph.add_node(end)

        self.graph.start_from(start)
    def test_bfs_found(self):
        self.assertEqual(self.graph.bfs("end"),True)
    def test_bfs_not_found(self):
        self.assertEqual(self.graph.bfs("c"),False)
    def test_bfs_generated_route(self):
        self.graph.bfs("end")
        self.assertEqual(self.graph.get_route(),["start", "A", "end"])

if __name__ == '__main__':
    unittest.main()
