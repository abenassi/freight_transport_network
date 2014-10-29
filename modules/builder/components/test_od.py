import unittest
from railway_link import Link
from od import OD


class ODTestCase(unittest.TestCase):
    """Test construction of od pair."""

    def setUp(self):
        self.od = OD("70-68", 333906, "068-069-070", "ancha")

    def test_nodes(self):
        self.assertEqual(self.od.nodes, [70, 68])

    def test_path(self):
        self.assertEqual(self.od.path, "068-069-070")

    def test_path_nodes(self):
        self.assertEqual(self.od.path_nodes, [68, 69, 70])

    def test_links(self):
        self.assertEqual(self.od.links, ['68-69', '69-70'])


def main():
    unittest.main()

if __name__ == '__main__':
    main()