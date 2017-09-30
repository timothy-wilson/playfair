#!/usr/bin/python3.6
"""
Goals for CLI:
- can pass in key as argv (python3 playfair PLAYFAIRKEY)
- can pass in -d for decrypt, will encrypt by default.

if "python3 playfair.py mysupersecretkey -d"
then sys.argv = ['playfair.py', 'mysupersecretkey', '-d']

- once program runs, it asks for input of plaintext or ciphertext.

eventually -- want a verbose mode that shows the steps of encryptions
"""
import playfair, sys

encrypt = True
key = 'BATMANANDROBIN'
file_name = ''
verbose = False
message = ''

def parse_args():
    global key, encrypt, file_name, verbose, message

    if '-h' in sys.argv:
        exit(
        ''' usage: ./cli.py [options]
            example ./cli.py -k EVERYTHINGISAWESOME
        all flags:
        -d : will decrypt with the playfair cipher otherwise it will encrypt by default
        -f : indicates that the following string is the name of the file to encrypt
        -k : indicates that the following string is the key for the playfair cipher (The default value is 'BATMANANDROBIN')
        -h : will print this to tell you how the program works
        -m : indicates that the following string is the plaintext or ciphertext (If no message is entered the program will ask to enter a message.)
        -v : will use a verbose mode showing the encryption proccess step by step
        the verbose mode will not work on files.
        '''
        )
    if '-k' in sys.argv:
        key = sys.argv[sys.argv.index('-k') + 1].upper()

    encrypt = not '-d' in sys.argv

    if '-f' in sys.argv:
        file_name = sys.argv[sys.argv.index('-f') + 1]
    if '-v' in sys.argv:
        if not file_name:
            verbose = True

    if '-m' in sys.argv:
        message = sys.argv[sys.argv.index('-m') + 1].upper()

def translate_file():
    import os
    if not os.path.exists(file_name):
        new_file_name = input('the file you want to encrypt does not exist, enter a new filename\n> ')
        return (translate_file(new_file_name, key))
    with open('ctf.txt', 'w') as ctf:
        with open(file_name, 'r') as ptf:
            if encrypt:
                ctf.write(playfair.encrypt_message(ptf.read(), key))
            else:
                ctf.write(playfair.decrypt_message(ptf.read(), key))

def encrypt_or_decrypt():
    if encrypt:
        text_type = 'plaintext'
        func = playfair.encrypt_message
    else:
        text_type = 'ciphertext'
        func = playfair.decrypt_message

    if message:
        print(func(message, key, verbose))
        exit()
    else:
        text = input(f'enter your {text_type}\n> ')
        if text == '':
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
