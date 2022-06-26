import base64
import re
from uuid import uuid4
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder="static", static_folder="static/asset")


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":

        with open("static/asset/37e139897f694251ab6c01a20202e6aa.png", "rb") as image_file:
            binary_file = image_file.read()
            decoded_bina = base64.encodebytes(binary_file)
            image_url = decoded_bina.decode("utf-8")
            print(image_url)
        return render_template('index.html')
    if request.method == "POST":
        f = request.json['file']
        t = request.json['type']
        f = clean_file(f, t)
        decoded = f.encode('utf-8')
        with open(write_file(t), 'wb') as output_file:
            decoded = base64.decodebytes(decoded)
            output_file.write(decoded)
        return jsonify({"status": "success"}), 200


def clean_file(file, file_type):
    if file_type == "png":
        f = re.sub('^data:image/.+;base64,', '', file)
    if file_type == "mkv":
        f = re.sub('^data:video/.+;base64,', '', file)
    return f

def write_file(file_type):
    return f"/static/asset/{uuid4().hex}.{file_type}"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)



 