def selection_sort(array: list):
	for i in range(len(array)):
		min_index = i
		for j in range(i+1,len(array)):
			if array[j] < array[min_index]:
				min_index = j
		temp = array[i]
		array[i] = array[min_index]
		array[min_index] = temp
	return(array) 

arr = input('Enter a list to sort in ascending order: ').split(',')
for i in range(len(arr)):
	arr[i] = float(arr[i])
print(selection_sort(arr))

 	