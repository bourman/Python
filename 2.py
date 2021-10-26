import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def test():
    with open('c:/users/user/desktop/file/1.TXT') as f:
        while(True):
            input("hello")


if __name__ == "__main__":
    app.run(debug=True)