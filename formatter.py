def grid_formatter(grid):
    format_grid = '''\n'''

    for row in grid:
        format_grid += '   '.join(row)
        format_grid += '\n\n'

    return format_grid

# def details(message, mode):
#     simple_pairs = []
#     for num in range(0, len(char_seq), 2):
#         simple_pairs.append(char_seq[num] + char_seq[num + 1])
#
#     if mode == 'List':
#         return simple_pairs
#     else:
#         fancy_string = ''''''
#         fancy_string += message
#         fancy_string += '\n\n'
#         fancy_string += ' '.join(simple_pairs)
#         fancy_string += '\n\n'

def details(pairs):
    return ' '.join(pairs)
