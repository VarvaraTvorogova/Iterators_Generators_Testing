import unittest

from RangeIterator_RangeGenerator import RangeIterator


class IteratorsTest(unittest.TestCase):

    def test_on_usual_range(self):
        exampl = RangeIterator(3)
        self.assertEqual(next(exampl), 0)
        self.assertEqual(next(exampl), 1)
        self.assertEqual(next(exampl), 2)
        self.assertRaises(StopIteration, next, exampl)
        self.assertEqual(exampl[2], 2)

    def test_on_empty_range(self):
        exampl = RangeIterator(0)
        self.assertRaises(StopIteration, next, exampl)

    def test_on_negative_range(self):
        exampl = RangeIterator(4, -15, -2)
        self.assertGreater(exampl[0], exampl[1])

    def test_of_resulting_list_with_big_steps(self):
        exampl = RangeIterator(5, 7, 18)
        self.assertEqual(next(exampl), 5)
        self.assertRaises(StopIteration, next, exampl)

    def test_on_range_with_two_arguments(self):
        exampl = RangeIterator(2, 5)
        self.assertEqual(next(exampl), 2)
        self.assertEqual(next(exampl), 3)
        self.assertEqual(next(exampl), 4)
        self.assertRaises(StopIteration, next, exampl)

    def test_on_range_without_agruments(self):
        with self.assertRaises(Exception, msg='At least one argument required'):
            exampl = RangeIterator()

    def test_on_range_with_zero_third_argument(self):
        with self.assertRaises(Exception, msg='Third arg must not be zero'):
            exampl = RangeIterator(1, 9, 0)


from RangeIterator_RangeGenerator import RangeGenerator


class GeneratorsTest(unittest.TestCase):

    def test_on_usual_range(self):
        exampl = RangeGenerator(3)
        self.assertEqual(exampl[2], 2)

    def test_on_empty_range(self):
        exampl = RangeGenerator(0)
        exampl_lst = []
        for i in exampl:
            exampl_lst.append(i)
        self.assertEqual(len(exampl_lst), 0)

    def test_on_negative_range(self):
        exampl = RangeGenerator(4, -15, -2)
        self.assertGreater(exampl[0], exampl[1])

    def test_of_resulting_list_with_big_steps(self):
        exampl = RangeGenerator(5, 7, 18)
        exampl_lst = []
        for i in exampl:
            exampl_lst.append(i)
        self.assertNotIn(19, exampl_lst)
        self.assertIn(5, exampl_lst)

    def test_on_range_with_two_arguments(self):
        exampl = RangeGenerator(2, 5)
        self.assertEqual(exampl[2], 4)

    def test_on_range_without_agruments(self):
        exampl = RangeGenerator
        self.assertRaises(Exception, msg='At least one argument required')

    def test_on_range_with_zero_third_argument(self):
        with self.assertRaises(Exception, msg='Third arg must not be zero'):
            exampl = RangeGenerator(1, 9, 0)


from RangeIterator_RangeGenerator import genert


class GenertTest(unittest.TestCase):

    def test_on_usual_range(self):
        exampl = genert(3)
        exampl_lst = []
        for i in exampl:
            exampl_lst.append(i)
        self.assertEqual(exampl_lst[2], 2)

    def test_on_empty_range(self):
        exampl = genert(0)
        exampl_lst = []
        for i in exampl:
            exampl_lst.append(i)
        self.assertEqual(len(exampl_lst), 0)

    def test_on_negative_range(self):
        exampl = genert(4, -15, -2)
        exampl_lst = []
        for i in exampl:
            exampl_lst.append(i)
        self.assertGreater(exampl_lst[0], exampl_lst[1])

    def test_of_resulting_list_with_big_steps(self):
        exampl = genert(5, 7, 18)
        exampl_lst = []
        for i in exampl:
            exampl_lst.append(i)
        self.assertNotIn(19, exampl_lst)
        self.assertIn(5, exampl_lst)

    def test_on_range_with_two_arguments(self):
        exampl = genert(2, 5)
        exampl_lst = []
        for i in exampl:
            exampl_lst.append(i)
        self.assertEqual(exampl_lst[2], 4)

    def test_on_range_without_agruments(self):
        with self.assertRaises(Exception, msg='At least one argument required'):
            exampl = genert()
            for i in exampl:
                pass

    def test_on_range_with_zero_third_argument(self):
        with self.assertRaises(Exception, msg='Third arg must not be zero'):
            exampl = genert(1, 9, 0)
            for i in exampl:
                pass


class RangeTest(unittest.TestCase):

    def test_on_usual_range(self):
        exampl = range(3)
        self.assertEqual(exampl[2], 2)

    def test_on_empty_range(self):
        exampl = range(0)
        exampl_lst = []
        for i in exampl:
            exampl_lst.append(i)
        self.assertEqual(len(exampl_lst), 0)

    def test_on_negative_range(self):
        exampl = range(4, -15, -2)
        self.assertGreater(exampl[0], exampl[1])

    def test_of_resulting_list_with_big_steps(self):
        exampl = range(5, 7, 18)
        exampl_lst = []
        for i in exampl:
            exampl_lst.append(i)
        self.assertNotIn(19, exampl_lst)
        self.assertIn(5, exampl_lst)

    def test_on_range_with_two_arguments(self):
        exampl = range(2, 5)
        self.assertEqual(exampl[2], 4)

    def test_on_range_without_agruments(self):
        with self.assertRaises(Exception, msg='range expected 1 arguments, got 0'):
            exampl = range()

    def test_on_range_with_zero_third_argument(self):
        with self.assertRaises(Exception, msg='range() arg 3 must not be zero'):
            exampl = RangeGenerator(1, 9, 0)


if __name__ == '__main__':
    unittest.main()
