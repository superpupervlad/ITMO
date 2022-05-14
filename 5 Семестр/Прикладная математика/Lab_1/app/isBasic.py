def is_basic(column):
    return sum(column) == 1 and len([c for c in column if c == 0]) == len(column) - 1