import random
import timeit

def iterate(l):

	counter = 0
	for i in range(len(l)):
		counter += 1


arr = [random.randint(0, 9999999) for i in range(10000000)]
arr_sorted = sorted(arr)

print(timeit.timeit('iterate(arr)', number=10, setup='from __main__ import iterate, arr'))
print(timeit.timeit('iterate(arr_sorted)', number=10, setup='from __main__ import iterate, arr_sorted'))