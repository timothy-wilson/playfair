def format_grid(grid):
    format_grid = '''\n'''

    for row in grid:
        format_grid += '   '.join(row)
        format_grid += '\n\n'

    return format_grid

def format_pairs(pairs):
    return ' '.join(pairs)
