# A prime number is a number greater than 1 that can be divided uniquely by 1 and itself


def prime(n):
	if n > 1:
		for i in range(2, n):
			if n % i == 0:
				print(f"The number {n} is not prime")
				break
		else:
			print(f"The number {n} is prime")
	else:
		print(f"The number {n} is not prime")


if __name__ == "__main__":
	while 1:
		number = (input("Type a number >>> "))
		try:
			prime(int(number))
		except ValueError:
			print("Please type an integer number")
			continue
