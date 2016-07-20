def shape(vector):
    return (len(vector),)


def vector_add(a, b):
    if len(a) == len(b):
        return [a[index] + b[index] for index in range(len(a))]
    else:
        raise ShapeError


def vector_sub(a, b):
    if len(a) == len(b):
        return [a[index] - b[index] for index in range(len(a))]
    else:
        raise ShapeError


def compare_shapes(*args):
    return len({shape(item) for item in args}) == 1


def vector_sum(*args):
    if compare_shapes(*args):
        return [sum(arg) for arg in zip(*args)]
    else:
        raise ShapeError


def dot(a, b):
    if compare_shapes(a, b):
        return sum([x * y for x, y in zip(a, b)])
    else:
        raise ShapeError


def vector_multiply(a, b):
    return [x * b for x in a]


def vector_mean(*args):
    return [sum(arg) / len(arg) for arg in zip(*args)]


def magnitude(a):
    return sum([item ** 2 for item in a]) ** 0.5


class ShapeError(Exception):
    pass
