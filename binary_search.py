def binary_search(item_list,item):
	first = 0  # avalin index va akharin index moarefi mikonim,
	last = len(item_list)-1   # chonshomaresh index az 0 shoroe mishavad pas akhrin index yek adad kamtar az lenght list ast
	found = False
	while( first<=last and not found):   # ta moghe avalin kamtar ya mosavi akhari hast va found false hast
		mid = (first + last)//2  # age miangin do adad floor division bar 2 ba item barabar shod, found true kon
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