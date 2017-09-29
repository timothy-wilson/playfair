import formatter

grid = [
['P', 'L', 'A', 'Y', 'F'],
['I', 'R', 'K', 'E', 'B'],
['C', 'D', 'G', 'H', 'M'],
['N', 'O', 'Q', 'S', 'T'],
['U', 'V', 'W', 'X', 'Z'],
]

def test_grid_formatter():

    result = formatter.grid_formatter(grid)

    assert result == '''
P   L   A   Y   F

I   R   K   E   B

C   D   G   H   M

N   O   Q   S   T

U   V   W   X   Z

'''

def test_details():

    message = ['TH','ED','RY','FI','SH','SW','IM','SA','LO','NE']
    result = formatter.details(message)

    assert result == 'TH ED RY FI SH SW IM SA LO NE'
