""" utilities.py
Provides simple python 2.x/3 compatability utilites

get_input provides a cross version method of getting user input
"""

import unittest


def get_input(prompt=""):
    
    """ Returns input entered from command prompt.
    
    Allows using either Python 2.x or 3.x as needed.
    
    Args:
        prompt: Prompt to display when requesting input (optional)
    
    Returns:
        User provided raw input from command line.
    """ 
    try:
        input_line = raw_input(prompt)
    except NameError:
        input_line = input(prompt)
    return input_line


            
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
