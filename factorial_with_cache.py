import time
cache = {}


def factorial(num):
	if num == 0 or num == 1:
		return 1
	if num in cache:
		return(cache[num])
	else:
		cache[num] = num*factorial(num-1)
		return(cache[num])


	

num1 = int(input('Enter a number to calculate its factorial: '))
print(factorial(num1))

num2 = int(input('Enter a number to calculate its factorial: '))
print(factorial(num2))

num3 = int(input('Enter a number to calculate its factorial: '))
t1 = time.time()
print(factorial(num3))
t2 = time.time()-t1
print(t2)