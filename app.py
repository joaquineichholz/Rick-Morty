from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    episodes_list = [[1, 2, 3, 4], [1, 3, 4, 5], [5, 5, 6, 7]]

    return render_template('index.html', list=episodes_list)

if __name__ == '__main__':
    app.run()