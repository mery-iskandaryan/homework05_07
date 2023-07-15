def digit_sum(num):
	if num == 0:
		return(0)
	return(num%10 + digit_sum(int(num/10)))

num = int(input('Enter a number to calculate its sum of digits: '))
print(digit_sum(num))