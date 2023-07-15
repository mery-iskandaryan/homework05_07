import time

def factorial(num):
	if num == 0 or num == 1:
		return 1
	else:
		return  num*factorial(num-1)


num3 = int(input('Enter a number to calculate its factorial: '))
t1 = time.time()
print(factorial(num3))
t2 = time.time()-t1
print(t2)