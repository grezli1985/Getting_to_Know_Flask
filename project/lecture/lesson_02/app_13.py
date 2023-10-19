from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = b"d8374aa1f8f457c0889754077746ee535dd53cab906908131d9f055da80d3e6b"


@app.route("/")
def index():
    return "Hi!"


@app.route("/form/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Проверка данных формы
        if not request.form["name"]:
            flash("Введите имя!", "danger")
            return redirect(url_for("form"))
        # Обработка данных формы
        flash("Форма успешно отправлена!", "success")
        return redirect(url_for("form"))
    return render_template("flash_form.html")

if __name__ == "__main__":
    app.run(debug=True)
