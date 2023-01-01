def sort_binary_list(lst):
	"""
	A function to sort binary list
	:param lst: A list containing binary numbers
	:return: A sorted binary list
	"""
	size = len(lst)
	mid = 0
	j = size - 1
	while(mid <= j):
		if lst[mid] == 0:
			mid+=1
		else:
			lst[mid], lst[j] = lst[j], lst[mid]
			j-=1
	return lst

print(sort_binary_list([0,0,1,0,1,0,1,0,1,1,1]))