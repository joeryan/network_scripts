""" utilities.py
Provides simple python 2.x/3 compatability utilites

get_input provides a cross version method of getting user input
"""
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
	            
