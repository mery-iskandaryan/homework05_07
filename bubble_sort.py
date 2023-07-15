def bubble_sort(array: list):
	counter = 0
	while counter < len(array)-1:
		counter = 0
		for i in range(len(array)):
			if i != len(array) - 1:
				if array[i] > array[i+1]:
					temp = array[i+1]
					array[i+1] = array[i]
					array[i] = temp
				else:
					counter += 1
	return array

arr = input('Enter a list of numbers to sort it in ascending order: ').split(',')
for i in range(len(arr)):
	arr[i] = int(arr[i])
	


print(bubble_sort(arr))