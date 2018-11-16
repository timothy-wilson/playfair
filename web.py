# export FLASK_APP=web.py
# flask run
from flask import Flask, request, render_template
import playfair

app = Flask(__name__)


@app.route('/')
def homescreen():
    return render_template('home.html')


@app.route('/translater', methods=['GET', 'POST'])
def translater():
    if request.method == 'GET':
        return render_template('translater.html')
    elif request.method == 'POST':
        text = request.form.get('inputtext')
        key = request.form.get('key')
        direction = request.form.get('direction')
        if direction == 'encrypt':
            encrypted = playfair.encrypt_message(text, key)
            message = f'You encrypted {text} with the key {key} and the result is {encrypted}'
            return render_template('translater.html', returntext=message)
        elif direction == 'decrypt':
            decrypted = playfair.decrypt_message(text, key)
            message = f'You decrypted {text} with the key {key} and the plaintext was '
            return render_template('translater.html', returntext=message+decrypted)
        else:
            message = 'You did not select encrypt or decrypt'
            return render_template('translater.html', returntext=message)
