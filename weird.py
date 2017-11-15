#Author - C3NZ
#Comparing sorted lists vs unsorted lists seems to yield weird results

import random
import timeit

#All this does is iterate through an unsorted list and then a sorted one
#okay... results show nothing weird
def iterate(l):

	counter = 0
	for i in range(len(l)):
		counter += 1


arr = [random.randint(0, 9999999) for i in range(10000000)]
arr_sorted = sorted(arr)

print(timeit.timeit('iterate(arr)', number=10, setup='from __main__ import iterate, arr'))
print(timeit.timeit('iterate(arr_sorted)', number=10, setup='from __main__ import iterate, arr_sorted'))


print("\nNow comparing items within the list\n")

#But when we add one simple logical comparison...
#Results get strange
def weird_iterate(l):

	counter = 0
	for i in range(len(l)):
		if l[i] > 100000
			counter += 1

print(timeit.timeit('weird_iterate(arr)', number=10, setup='from __main__ import weird_iterate, arr'))
print(timeit.timeit('weird_iterate(arr_sorted)', number=10, setup='from __main__ import weird_iterate, arr_sorted'))