import os
import unittest
import logging
from algo.graph import DFS

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


class TestBase(unittest.TestCase):

    def test_traverse(self):
        graph = {
            'A': set(['B', 'C', 'F']),
            'B': set(['A', 'D', 'E']),
            'C': set(['A', 'F']),
            'D': set(['B']),
            'E': set(['B', 'F']),
            'F': set(['A', 'C', 'E'])
        }

        graph_obj = DFS(graph)
        visited = graph_obj.traverse('A')

        self.assertEqual(visited, ['A', 'C', 'F', 'E', 'B', 'D'])


if __name__ == '__main__':
    unittest.main()
