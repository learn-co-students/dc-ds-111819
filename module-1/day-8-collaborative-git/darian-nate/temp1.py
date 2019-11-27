def is_short(x, n = 8):
    return len(x) < n
short_names = list(filter(is_short, names))