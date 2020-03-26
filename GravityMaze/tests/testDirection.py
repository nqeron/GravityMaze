import unittest
from GravityMaze.GravityGame import Direction


class TestDirectionEnum(unittest.TestCase):

    def test_sets(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_opposite(self):
        self.assertEqual(Direction.get_opposite(Direction.DOWN), Direction.UP)
        self.assertEqual(Direction.LEFT, Direction.get_opposite(Direction.RIGHT))
        self.assertEqual(Direction.DOWN, Direction.get_opposite(Direction.UP))
        self.assertEqual(Direction.RIGHT, Direction.get_opposite(Direction.LEFT))


if __name__ == '__main__':
    unittest.main()
