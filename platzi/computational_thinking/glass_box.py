import unittest


def is_years_older(age: int) -> bool:
    return True if age >= 18 else False


class GlassBoxTest(unittest.TestCase):
    def test_is_of_legal_age(self) -> None:
        age = 20

        result = is_years_older(age)

        self.assertEqual(result, True)

    def test_is_minor_age(self) -> None:
        age = 15

        result = is_years_older(age)

        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
