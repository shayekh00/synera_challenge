# Integration test for the full graph

import unittest
from graph import Graph

class TestFullGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_add_nodes(self):
        self.graph.add_node('A')
        self.graph.add_node('B')
        self.assertIn('A', self.graph.nodes)
        self.assertIn('B', self.graph.nodes)

    def test_add_edges(self):
        self.graph.add_node('A')
        self.graph.add_node('B')
        self.graph.add_edge('A', 'B')
        self.assertIn('B', self.graph.edges['A'])

    def test_remove_node(self):
        self.graph.add_node('A')
        self.graph.remove_node('A')
        self.assertNotIn('A', self.graph.nodes)

    def test_remove_edge(self):
        self.graph.add_node('A')
        self.graph.add_node('B')
        self.graph.add_edge('A', 'B')
        self.graph.remove_edge('A', 'B')
        self.assertNotIn('B', self.graph.edges['A'])

    def test_find_path(self):
        self.graph.add_node('A')
        self.graph.add_node('B')
        self.graph.add_node('C')
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('B', 'C')
        path = self.graph.find_path('A', 'C')
        self.assertEqual(path, ['A', 'B', 'C'])

if __name__ == '__main__':
    unittest.main()