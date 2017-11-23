import formatter

grid = [
['P', 'L', 'A', 'Y', 'F'],
['I', 'R', 'K', 'E', 'B'],
['C', 'D', 'G', 'H', 'M'],
['N', 'O', 'Q', 'S', 'T'],
['U', 'V', 'W', 'X', 'Z'],
]

def test_grid_formatter():

    result = formatter.format_grid(grid)

    assert result == '''
P   L   A   Y   F

I   R   K   E   B

C   D   G   H   M

N   O   Q   S   T

U   V   W   X   Z

'''

def test_details():

    message = ['TH','ED','RY','FI','SH','SW','IM','SA','LO','NE']
    result = formatter.format_pairs(message)

    assert result == 'TH ED RY FI SH SW IM SA LO NE'
