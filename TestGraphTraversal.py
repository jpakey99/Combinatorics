import unittest
import GraphTraversal


class TestGraphTraversal(unittest.TestCase):
    def testTwoNodesThreeCycles(self):
        possibilities = {
            'A': ['B', 'A'],
            'B': ['A', 'B'],
        }
        GraphTraversal.new_g(1, 'A', 'A', 0, '', possibilities)
        self.assertEqual(GraphTraversal.get_total(), 1)
        GraphTraversal.new_g(2, 'A', 'A', 0, '', possibilities)
        self.assertEqual(GraphTraversal.get_total(), 2)
        GraphTraversal.new_g(3, 'A', 'A', 0, '', possibilities)
        self.assertEqual(GraphTraversal.get_total(), 4)
        GraphTraversal.new_g(4, 'A', 'A', 0, '', possibilities)
        self.assertEqual(GraphTraversal.get_total(), 8)
        GraphTraversal.new_g(0, 'A', 'A', 0, '', possibilities)
        self.assertEqual(GraphTraversal.get_total(), 0)



if __name__ == '__main__':
    unittest.main()
