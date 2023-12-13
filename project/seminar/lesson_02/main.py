from pathlib import PurePath, Path

from flask import Flask, render_template, request, abort, flash, url_for
from werkzeug.utils import secure_filename, redirect

app = Flask(__name__)
app.secret_key = b"5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello/")
def hello():
    name = "Bob"
    return f"Hello, {name}"


@app.route("/upload/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files.get("file")
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), "uploads", file_name))
        return f"Файл {file_name} загружен на сервер"
    return render_template("upload.html")


users = ["John", "Olga"]
info = {"John": "123", "Olga": "321"}


@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username in users and password == info[username]:
            return f"Hello, {username}"
    return render_template("login.html")


@app.route("/text/", methods=["GET", "POST"])
def text():
    if request.method == "POST":
        texts = request.form.get("text")
        if texts:
            return f"Количество слов: {len(texts.split())}"
    return render_template("text.html")


@app.route("/calc/", methods=["GET", "POST"])
def calc():
    if request.method == "POST":
        num1 = int(request.form.get("num1"))
        num2 = int(request.form.get("num2"))
        operation = request.form.get("operation")
        if operation == "add":
            return f"Сумма равна {num1 + num2}"
        if operation == "subtract":
            return f"Сумма равна {num1 - num2}"
        if operation == "multiply":
            return f"Сумма равна {num1 * num2}"
        if operation == "divide":
            return f"Сумма равна {num1 / num2}"
    return render_template("calc.html")


@app.route("/check_age", methods=["GET", "POST"])
def check_age():
    if request.method == "POST":
        name = request.form.get("name")
        age = int(request.form.get("age"))
        if age >= 18:
            return redirect("result")
        else:
            abort(403)
    return render_template("check_age.html")


@app.route("/result/")
def result():
    return f"<h1>Добро пожаловать!</h1>"


@app.errorhandler(403)
def forbidden(e):
    context = {
        "title": "Доступ запрещен",
        "url": request.base_url,
    }
    return render_template("403.html", **context), 403


@app.route('/redirect/')
def redirect_to_index():
    return redirect(url_for('index'))


@app.route("/flash", methods=["GET", "POST"])
def _flash():
    if request.method == "POST":
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('_flash'))
        name = request.form.get("name")
        flash(f"Привет {name}", "success")
        return redirect(url_for("_flash"))

    return render_template("flash.html")


if __name__ == "__main__":
    app.run(debug=True)
