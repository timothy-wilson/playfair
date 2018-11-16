#!/usr/bin/python3.6
import os, sys

import playfair

encrypt = True
key = 'BATMANANDROBIN'
file_name = ''
verbose = False
message = ''


def parse_args():
    global key, encrypt, file_name, verbose, message

    if '-h' in sys.argv:
        exit('''
usage: ./cli.py [options]
example ./cli.py -k EVERYTHINGISAWESOME
all flags:
-d : will decrypt with the playfair cipher; it will encrypt by default
-f : indicates that the following string is the name of the file to encrypt
-k : indicates that the following string is the key for the playfair cipher
     The default value is 'BATMANANDROBIN'
-h : help text
-m : indicates that the following string is the plaintext or ciphertext
     If no message is entered the program will ask to enter a message.
-v : will use a verbose mode showing the encryption proccess step by step;
     the verbose mode will not work on files.
''')
    if '-k' in sys.argv:
        if sys.argv[-1] == '-k':
            exit("you need to pass in some text after '-k'")
        else:
            key = ''.join(sys.argv[sys.argv.index('-k') + 1].upper())

    encrypt = not '-d' in sys.argv

    if '-f' in sys.argv:
        if sys.argv[-1] == '-f':
            exit("you need to pass in a file name after '-f'")
        file_name = sys.argv[sys.argv.index('-f') + 1]

    if '-v' in sys.argv:
        if not file_name:
            verbose = True

    if '-m' in sys.argv:
        if sys.argv[-1] == '-m':
                exit("you need to pass in some text after '-m'")
        else:
            for i in range(sys.argv.index('-m') + 1, len(sys.argv)):
                if not sys.argv[i].startswith('-'):
                    message += sys.argv[i]


def translate_file():
    if not os.path.exists(file_name):
        new_file_name = input('the file you want to encrypt does not exist, enter a new filename\n> ')
        return translate_file(new_file_name, key)
    output_fn = input('What would you like your encrypted or decrypted file to be named.\n>')
    with open(output_fn, 'w') as ctf:
        with open(file_name, 'r') as ptf:
            if encrypt:
                transformed = playfair.encrypt_message(ptf.read(), key)
            else:
                transformed = playfair.decrypt_message(ptf.read(), key)
            while transformed:
                ctf.write(transformed[0:80] + '\n')
                transformed = transformed[80:]
            print(f'encrypted to file {output_fn}')


def encrypt_or_decrypt():
    global message
    if encrypt:
        text_type = 'plaintext'
        func = playfair.encrypt_message
    else:
        text_type = 'ciphertext'
        func = playfair.decrypt_message

    if message:
        print(func(message, key, verbose))
        message = ''
    try:
        text = input(f'enter your {text_type}\n> ')
    except KeyboardInterrupt:
        exit()

    print(func(text, key, verbose))
    print()

def main():
    parse_args()
    if file_name:
        translate_file()
    else:
        while True:
            encrypt_or_decrypt()


if __name__ == '__main__':
    main()
