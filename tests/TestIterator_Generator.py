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
        self.assertNotIn(19, exampl)
        self.assertEqual(exampl.lst, [5])

    def test_on_range_with_two_arguments (self):
        exampl = RangeIterator (2, 5)
        self.assertEqual(next(exampl), 2)
        self.assertEqual(next(exampl), 3)
        self.assertEqual(next(exampl), 4)
        self.assertRaises(StopIteration, next, exampl)

    def test_on_range_without_agruments (self):
        exampl = RangeIterator
        self.assertRaises(Exception, msg = 'At least one argument required')

#    def test_on_range_with_zero_third_argument (self):
#       exampl = RangeIterator (1, 9, 0)
#      self.assertRaises(Exception, msg = 'Third arg must not be zero')



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
        self.assertNotIn(19, exampl)
        self.assertEqual(exampl.lst, [5])

    def test_on_range_with_two_arguments(self):
        exampl = RangeGenerator(2, 5)
        self.assertEqual(exampl [2], 4)

    def test_on_range_without_agruments(self):
        exampl = RangeGenerator
        self.assertRaises(Exception, msg='At least one argument required')

#    def test_on_range_with_zero_third_argument (self):
#      exampl = RangeIterator (1, 9, 0)
#      self.assertRaises(Exception, msg = 'Third arg must not be zero')

if __name__ == '__main__':
    unittest.main()


