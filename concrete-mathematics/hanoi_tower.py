# TODO: hanoi tower

def estimate_complexity(n):
    return 0 if n == 0 else 2 * estimate_complexity(n-1) + 1
