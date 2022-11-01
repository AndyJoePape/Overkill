from flask import Flask, request
from encrypt import encryptPlainText
from decrypt import decryptPlainText

app = Flask(__name__)

plain_text = "PLAIN_TEXT"
cipher_text = "CIPHER_TEXT"


@app.route("/")
def health_check():
    return {"version": "1.0.0"}


@app.route("/encrypt")
def encrypt():
    headers = request.headers

    if not headers.get(plain_text):
        return f'[{plain_text}] header needed to encrypt', 400

    cipherText = encryptPlainText(headers.get(plain_text))
    return cipherText

@app.route("/decrypt")
def decrypt():
    headers = request.headers

    if not headers.get(cipher_text):
        return f'[{cipher_text}] header needed to encrypt', 400

    plainText = decryptPlainText(headers.get(cipher_text))
    return plainText


