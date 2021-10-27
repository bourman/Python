from flask import Flask
import os
app = Flask(__name__)


@app.route('/')

def index():
    with open(r'C:/users/ויקטור/desktop/txt/1.txt', 'r') as r:
        lines = r.readlines()
        return "--- Grop 1 ---<br>" + "".join(lines[0:3040]).replace("\n", "<br>") +\
               "--- Grop 2 ---<br>" + "".join(lines[3040:6080]).replace("\n", "<br>") +\
               "--- Grop 3 ---<br>" + "".join(lines[6080:9120]).replace("\n", "<br>") +\
               "--- Grop 4 ---<br>" + "".join(lines[9120:12160]).replace("\n", "<br>") +\
               "--- Grop 5 ---<br>" + "".join(lines[12160:15200]).replace("\n", "<br>") +\
               "--- Grop 6 ---<br>" + "".join(lines[15200:18240]).replace("\n", "<br>")


if __name__ == '__main__':
    app.run(debug=True)