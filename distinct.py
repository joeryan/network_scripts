import unittest

def distinct(iterable):
	""" Return unique items by elminiating duplicates.
	
	Args:
		iterable: the source series
		
	Yields:
		Unique elements in order from 'iterable'.
	"""
	
	seen = set()
	for item in iterable:
		if item in seen:
			continue
		yield item
		seen.add(item)
	

class TestCases(unittest.TestCase):
    def test_empty_iterable_raises_StopIteration_Error(self):
        empty_iter = distinct([])
        with self.assertRaises(StopIteration):
            next(empty_iter)
            
    def test_list_of_items_with_duplicates_returns_only_distinct_items(self):
        test_iter = distinct([5, 7, 7, 5, 6, 10, 5])
        self.assertEqual(5,  next(test_iter))
        self.assertEqual(7,  next(test_iter))
        self.assertEqual(6,  next(test_iter))
        self.assertEqual(10,  next(test_iter))
        with self.assertRaises(StopIteration):
            next(test_iter)
    
    def test_list_of_items_returns_correct_number_of_items(self):
        test_iter = distinct([5, 7, 7, 5, 6, 10, 5])
        count = 0
        for item in test_iter:
           count += 1
        self.assertEqual(4,  count)
        
if __name__ == '__main__':
	unittest.main()
