from random import randint
import time

def throw():
	a = randint(1,6)
	b = randint(1,6)
	return a+b


def single_game():
	print("Wykonujemy rzut: ")
	time.Sleep(1)
	t0 = throw()
	if t0 in [7, 11]:
		print("Wygrales!")
		return True
	elif t0 in [2, 3, 12]:
		print("Przegrałeś!")
		return False
	else:
		time.Sleep(1)
		print("Punkt: ", t0)


