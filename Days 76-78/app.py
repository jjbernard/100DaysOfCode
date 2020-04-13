from flask import Flask, render_template
from data import fav_food

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", fav_food=fav_food)


if __name__ == '__main__':
    app.run()
