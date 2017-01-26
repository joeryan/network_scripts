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
	
def run_distinct():
	items = [5,7,7,5,6,10,5]
	for item in distinct(items):
		print(item)
		

if __name__ == '__main__':
	run_distinct()