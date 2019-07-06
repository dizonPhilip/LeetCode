import unittest
from jump_game_ii import Solution

class TestJumpGame(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        board = [2,3,1,1,4]
        ret = solution.jump(board)
        self.assertEqual(2, ret)

    def test_2(self):
        solution = Solution()
        board = [3,2,0,1,1,4]
        ret = solution.jump(board)
        self.assertEqual(3, ret)

    def test_3(self):
        solution = Solution()
        board = [2,9,6,5,7,0,7,2,7,9,3,2,2,5,7,8,1,6,6,6,3,5,2,2,6,3]
        ret = solution.jump(board)
        self.assertEqual(5, ret)

    def test_4(self):
        solution = Solution()
        board = [0]
        ret = solution.jump(board)
        self.assertEqual(0, ret)

    def test_5(self):
        solution = Solution()
        board = [1,2]
        ret = solution.jump(board)
        self.assertEqual(1, ret)

    def test_6(self):
        solution = Solution()
        board = [3,1,2]
        ret = solution.jump(board)
        self.assertEqual(1, ret)

if __name__ == "__main__":
    unittest.main()