from flask import Flask, request
from encrypt import encryptPlainText
from decrypt import decryptPlainText
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

plain_text = "PLAIN_TEXT"
cipher_text = "CIPHER_TEXT"


@app.route("/")
def health_check():
    return {"version": "1.0.0"}


@app.route("/encrypt")
def encrypt():
    data = request.data

    if len(data) < 1:
        return "Data must contain the plaintext"

    return encryptPlainText(str(data)[2:-1])


@app.route("/header")
def header():
    return request.data


@app.route("/decrypt")
def decrypt():
    data = request.data

    if len(data) < 1:
        return "Data must contain the ciphertext"

    return decryptPlainText(str(data)[2:-1])
