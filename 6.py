import os
from flask import Flask
app = Flask(__name__)


@app.route('/test')
def riv_1():
    document_path = os.getcwd()+'temp.txt'
    document = open('c:/users/user/desktop/file1/1.TXT', 'r')
    return document.read()

if __name__ == '__main__':
    app.run(debug=True)