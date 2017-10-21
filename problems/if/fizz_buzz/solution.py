# encoding: utf-8

def is_multiple(num, divider):

	while num > 0:
		num -= divider

	is_divider = True if num == 0 else False

	return is_divider


def define_fbp(num):

	ans_str = ''
	# Больно так писать, но максимально приближено
	if is_multiple(num, 3):
		ans_str += 'Fizz'

	if is_multiple(num, 5):
		ans_str += 'Buzz'

	if is_multiple(num, 7):
		ans_str += 'Pozz'

	if ans_str == "":
		ans_str = "Nedelizz"

	return ans_str


if __name__ == '__main__':

		num = int(input())
		print(define_fbp(num))