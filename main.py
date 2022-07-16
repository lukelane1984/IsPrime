# checking if a number is prime
import os
import sys

running = bool(True)


def is_prime(num):
	# Check if given number is greater than 1, since 1 isn't considered a prime number
	if num > 1:

		# Iterate from 2 to n/2 using a for loop, adding 1 to num/2 with every iteration
		# until it either reaches a factor of the given  number, meaning it's not prime
		# But, if it iterates to the same value of the given number that means it can only be divided by itself
		# (or by 1) which means it's prime, by definition!!
		for i in range(2, int(num / 2) + 1):

			# If num is divisible by any number between
			# 2 and n / 2, it is not prime
			# By taking the modulus of i we can check if it can be divided into
			# a whole number.
			# So if the modulus = 0, we know it's not prime
			if (num % i) == 0:
				print("> ", num, "is NOT a prime number...")
				break
		else:
			print("> ", num, "is a prime number!")

	else:
		print("> ", num, "is NOT a prime number...")


def clear():
	os.system("clear")


def leave():
	sys.exit()


def titlebar():
	clear()
	print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
	print("┃                                              v0.9 by LukeLane1984  ┃")
	print("┃            _____     ______     _               ___                ┃")
	print("┃           |_   _|    | ___ \\   (_)             |__ \\               ┃")
	print("┃             | | ___  | |_/ / __ _ _ __ ___   ___  ) |              ┃")
	print("┃             | |/ __| |  __/ '__| | '_ ` _ \\ / _ \\/ /               ┃")
	print("┃            _| |\\__ \\ | |  | |  | | | | | | |  __/_|                ┃")
	print("┃            \\___/___/ \\_|  |_|  |_|_| |_| |_|\\___(_)                ┃")
	print("┃                                 Perhaps... Let's find out!         ┃")
	print("┃                                                                    ┃")
	print("┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")
	print("│             CHECK IF A NUMBER IS A PRIME NUMBER OR NOT             │")
	print("└────────────────────────────────────────────────────────────────────┘\n")


def main():
	print("Input number and press Enter to check if it's prime")
	# We get user input, but we do so by defining it as an integer, with int()
	# otherwise the input would be stored as a string/str
	number = int(input(">>> "))
	# run the is_prime() function with the 'number' variable
	is_prime(number)

# we start a while loop, so the script can be repeated and will only
# terminate once the 'running' variable is changed from True to False


while running:
	titlebar()
	main()
# here we ask the user if they want to do another check, or to end the script
	print("\nPress ENTER to check another number, or type \'end\' or \'exit\' to leave")
	end = input(">>> ")
# if the user inputs 'end' or 'exit' the variable 'running' will be changed to False
	if end == "exit" or end == "end":
		running = False

else:
	# if the variable 'running' is set to 'False', the while loop breaks and the script ends
	clear()
	print("-------------------------------------------")
	print("    CheckIfPrime v0.9 by LukeLane1984")
	print("-------------------------------------------")
	print("Script terminated\n\nHave a nice day!\n\n")
	leave()
