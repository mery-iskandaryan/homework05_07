def binary(num, sorted_list):
	mid_ind = len(sorted_list)//2
	low_ind = 0
	high_ind = len(sorted_list)-1

	while low_ind < high_ind:
		if num == sorted_list[low_ind]:
			return (low_ind)
			break
		elif num == sorted_list[high_ind]:
			return (high_ind)
			break
		if num > sorted_list[mid_ind]:
			low_ind = mid_ind + 1
			mid_ind = (low_ind + high_ind)//2
		elif num < sorted_list[mid_ind]:
			high_ind = mid_ind - 1
			mid_ind = (low_ind + high_ind)//2
		else:
			return (mid_ind)
			break
	return ('The number is not present in the list.')


ls = [0,1,2,3,5,7,16,18,21,32]
print(binary(21,ls))