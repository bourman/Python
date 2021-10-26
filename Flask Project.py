from time import sleep
from flask import Flask
import os

app = Flask(__name__)


@app.route("/name")
def test():
    with open("c:/users/user/desktop/file1/1.TXT") as f:
        return f.read()


if __name__ == "__main__":
    app.run(debug=True)


