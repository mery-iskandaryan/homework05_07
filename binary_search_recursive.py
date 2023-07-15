def binary_search_recursive(array, target, low, high):
	if low > high:
		print('The number is not present in the list.')
	else:
		mid = (low+high) // 2	
		if array[mid] == target:
			print('The index of the entered number is ',mid)
		elif array[mid] > target:
			binary_search_recursive(array, target, low, mid-1)
		elif array[mid] < target:
			binary_search_recursive(array, target, mid+1, high)


arr = input('Enter a list of numbers: ')
arr = arr.split(',')
for i in range(len(arr)):
	arr[i] = int(arr[i])
target = int(input('Enter the target number: '))
binary_search_recursive(arr, target, 0, len(arr)-1)