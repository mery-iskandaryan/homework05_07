def insertion_sort(array: list):
	for i in range(1, len(array)):
		temp = array[i]
		j = i -1 
		while (j>=0) and(temp<array[j]):
			array[j+1] = array[j]
			j -= 1
		array[j+1] = temp 
	return(array)

arr = input('Enter a list of numbers to sort it in ascending order: ').split(',')
for i in range(len(arr)):
	arr[i] = int(arr[i])
	
print(insertion_sort(arr))