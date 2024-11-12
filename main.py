from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/user/<name>')
def hello_user(name):
    return render_template('index.html', content = name, cars = ["BMW","Mercedes","Vinfast", "Tesla"])

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        user_name = request.form["name"]
        if user_name:
            return redirect(url_for("hello_user", name= user_name))
    return render_template("login.html")
if __name__ == "__main__":
    app.run(debug=True)