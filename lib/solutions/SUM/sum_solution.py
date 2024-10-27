# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if isinstance(x, int) and isinstance(y, int):
        if x > 100 or x < 0:
            raise ValueError("Input params between 0 and 100")
        else:
            return x + y
    else:
        raise ValueError("Input params are integers")


