import unittest

from perf_cache import fibonacci, memoize


class MemoizeTests(unittest.TestCase):
    def test_memoize_reuses_results(self):
        calls = 0

        @memoize
        def add(a: int, b: int) -> int:
            nonlocal calls
            calls += 1
            return a + b

        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(calls, 1)

    def test_fibonacci_is_cached(self):
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(20), 6765)


if __name__ == "__main__":
    unittest.main()
