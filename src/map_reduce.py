



def map_reduce(iterable, map_func, reduce_func, init):
	mapped = map(map_func, iterable)
	return reduce(reduce_func, mapped, init)


def map_reduce2(iterable, map_func, reduce_func, init):
	# map-reduce com list comprehension
	return reduce(reduce_func, [map_func(item) for item in iterable], init)

def executar(map_reduce_func):
	l = [[1,2,3,4], [2,3,4,5], [4,6,7]]
	return map_reduce_func(l, lambda lista: [2 * x for x in lista if x % 2 == 0], lambda acc, lista: acc + sum(lista), 0)

print executar(map_reduce)
print executar(map_reduce2)
