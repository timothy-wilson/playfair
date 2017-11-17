import formatter

def clean_plaintext(plaintext):
    '''Removes spaces and punctuation, converts to upper case.'''
    cleaned = []
    for ch in plaintext:
        if ch.isalpha():
            ch = ch.upper()
            if ch == 'J':
                ch = 'I'
            cleaned.append(ch)
    return cleaned

def build_grid(key):
    '''Creates 5x5 Playfair grid from all-caps key.'''
    clean_key = []
    for l in key:
        if l not in clean_key:
            clean_key.append(l)

    LETTERS = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    for l in LETTERS:
        if l not in clean_key:
            clean_key.append(l)

    grid = []
    for n in range(0, 21, 5):
        grid.append(clean_key[n:n + 5])

    return grid

def make_pairs_simple(char_seq):
    """ Breaks a message into pairs of characters """
    simple_pairs = []
    for num in range(0, len(char_seq), 2):
        if char_seq[-1] == char_seq[num]:
            exit('That is an invalid ciphertext')
        simple_pairs.append(char_seq[num] + char_seq[num + 1])

    return [s.upper() for s in simple_pairs]

def make_pairs_to_encrypt(char_seq):
    """ Given a sequence of characters, breaks it into pairs, two special cases:
    - Double letters: 'EE' -> 'EX'
    - Single letter on end: 'T' -> 'TX'

    This function should use make_pairs_simple. """
    if len(char_seq) % 2 == 1:
        char_seq.append('X')

    pairs_to_encrypt = make_pairs_simple(char_seq)
    ready_to_encrypt = []
    for i in pairs_to_encrypt:
        if i[0] == i[1]:
            ready_to_encrypt.append(i[0] + 'X')
        else:
            ready_to_encrypt.append(i)

    return ready_to_encrypt

def transform_pair(pair, grid, encrypt=True):
    """ Takes a pair, and transforms them into a different pair, using grid.
    By default, encrypts, to reverse, pass in encrypt=False """
    row1, column1 = find_cordinates(pair[0], grid)
    row2, column2 = find_cordinates(pair[1], grid)
    if column1 == column2:
        return(same_column_transform(encrypt, grid, row1, column1, row2, column2))
    elif row1 == row2:
        return(same_row_tranform(encrypt, grid, row1, column1, row2, column2))
    else:

        return grid[row1][column2] + grid[row2][column1]

def find_cordinates(letter, grid):
    for i in range(5):
        if letter in grid[i]:
            for j in range(5):
                if grid[i][j] == letter:
                    return i, j

def next_index(encrypt, index):
    if encrypt:
        number = 1
        end = 4
    else:
        number = -1
        end = 0
    return abs(end - 4) if index == end else index + number

def same_column_transform(encrypt, grid, row1, column1, row2, column2):

    return grid[next_index(encrypt, row1)][column1] + grid[next_index(encrypt, row2)][column2]

def same_row_tranform(encrypt, grid, row1, column1, row2, column2):

    return grid[row1][next_index(encrypt, column1)] + grid[row2][next_index(encrypt, column2)]

def transform_pairs(pairs, grid, encrypt=True):
    """ Takes a list of pairs, and calls transform_pair on each """


    return [transform_pair(p, grid, encrypt) for p in pairs]


def encrypt_message(message, key, verbose = False):
    """ Takes a message that may containt spaces, punctuation, and lowercase.

    Strips non-alphabetical characters, and uppercases letters, then encrypts. """
    new_message = clean_plaintext(message)
    ready_to_encrypt = make_pairs_to_encrypt(new_message)
    grid = build_grid(key.upper())
    pairs = transform_pairs(ready_to_encrypt, grid)

    if verbose:
        print(formatter.format_grid(grid))
        print(formatter.format_pairs(ready_to_encrypt))
        print('\n')
        print(formatter.format_pairs(pairs))
        print('\n')

    return ''.join(pairs)


def decrypt_check(pairs):
    for p in pairs:
        if p[0] == p[1]:
            exit('that is an invalid ciphertext.')


def decrypt_message(ciphertext, key, verbose = False):
    """ Takes an all-caps no-space ciphertext, returns an all-caps no-space plaintext. """
    grid = build_grid(key.upper())
    ready_to_decrypt = make_pairs_simple(ciphertext)
    decrypt_check()
    pairs = transform_pairs(ready_to_decrypt, grid, False)

    if verbose:
        print(formatter.format_grid(grid))
        print(formatter.format_pairs(ready_to_decrypt))
        print('\n')
        print(formatter.format_pairs(pairs))
        print('\n')

    return ''.join(pairs)
