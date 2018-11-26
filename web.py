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
            return render_template('translater.html', returntext=encrypted, mode=direction, key=key, inputtext=text)
        elif direction == 'decrypt':
            decrypted = playfair.decrypt_message(text, key)
            return render_template('translater.html', returntext=decrypted, mode=direction, key=key, inputtext=text)
        else:
            return render_template('translater.html')


@app.route('/about')
def about():
    return render_template("about.html")
