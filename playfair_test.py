import playfair


grid = [
    ['P', 'L', 'A', 'Y', 'F'],
    ['I', 'R', 'K', 'E', 'B'],
    ['C', 'D', 'G', 'H', 'M'],
    ['N', 'O', 'Q', 'S', 'T'],
    ['U', 'V', 'W', 'X', 'Z'],
]


def test_clean_plaintext():
    plaintext = 'Justice will prevail!'

    result = playfair.clean_plaintext(plaintext)

    assert result == list('IUSTICEWILLPREVAIL')


def test_build_grid():
    key = 'PLAYFAIRKEY'

    result = playfair.build_grid(key)

    assert result == grid


def test_make_pairs_simple():
    """Put them in pairs, without any special cases"""
    clean_plaintext = ['S', 'C', 'R', 'A', 'M', 'B', 'L', 'E']

    result = playfair.make_pairs_simple(clean_plaintext)

    assert result == ['SC', 'RA', 'MB', 'LE']


def test_make_pairs_encrypt():
    """Put them in pairs, with two special cases:
        - double letters result in 'X': 'TT' -> 'TX'
        - one letter at end gets 'X' added: 'K' -> 'KX'
    """
    clean_plaintext = ['I', 'A', 'T', 'T', 'A', 'C', 'K']

    result = playfair.make_pairs_to_encrypt(clean_plaintext)

    assert result == ['IA', 'TX', 'AC', 'KX']

def test_encrypt_pair_regular():
    """The usual way that a pair get's encrypted"""
    pair = 'RA'

    result = playfair.transform_pair(pair, grid)

    assert result == 'KL'


def test_encrypt_pair_column():
    """Special case for letters in same column"""
    pair = 'AW'

    result = playfair.transform_pair(pair, grid,)

    assert result == 'KA'


def test_encrypt_pair_row():
    """Special case for letters in same row"""
    pair = 'KI'

    result = playfair.transform_pair(pair, grid,)

    assert result == 'ER'


def test_encrypt_pairs():
    pairs = ['RA', 'AW', 'KI']

    result = playfair.transform_pairs(pairs, grid)

    assert result == ['KL','KA','ER']


def test_encrypt_message():
    message = 'Attack the eastern hill at night.'
    key = 'PLAYFAIRKEY'

    result = playfair.encrypt_message(message, key)

    assert result == 'FQQFGISMHYYQSBIOCEYVFQUCHMSZ'


def test_decrypt_message():
    ciphertext = 'FQQFGISMHYYQSBIOCEYVFQUCHMSZ'
    key = 'PLAYFAIRKEY'

    result = playfair.decrypt_message(ciphertext, key)

    assert result == 'ATTACKTHEXASTERNHILXATNIGHTX'
