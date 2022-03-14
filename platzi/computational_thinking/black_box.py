import unittest


def sum_2_numbers(num_1: int, num_2: int) -> int:
    return num_1 +  num_2


class BlackBoxTest(unittest.TestCase):

    def test_sum_2_positives(self) -> None:
        num_1 = 10
        num_2 = 5
        
        result = sum_2_numbers(num_1, num_2)

        self.assertEqual(result, 15)

    def test_sum_2_negatives(self) -> None:
        num_1 = -10
        num_2 = -7

        result = sum_2_numbers(num_1, num_2)

        self.assertEqual(result, -17)


if __name__ == "__main__":
    unittest.main()
