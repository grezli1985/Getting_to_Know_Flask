from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def root():
    return render_template("Одежда.html")


@app.get("/Куртка/")
def students():
    return render_template("Куртка.html")


@app.get("/Обувь/")
def news():
    return render_template("Обувь.html")


if __name__ == "__main__":
    app.run(debug=True)
