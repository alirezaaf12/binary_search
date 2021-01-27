def binary_search(item_list,item):
	first = 0  
	last = len(item_list)-1   
	found = False
	while( first<=last and not found):   
		mid = (first + last)//2  
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found

my_list = [3, 6, 9, 13, 17, 25, 30, 50, 70, 90]

print(binary_search(my_list, 25))
