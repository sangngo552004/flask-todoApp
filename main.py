from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.config["SECRET_KEY"] = "0374164299"
app.permanent_session_lifetime = timedelta(seconds=60)
@app.route('/user')
def user():
    if "user" in session:
        user_name = session["user"]
        return render_template('index.html', content = user_name, cars = ["BMW","Mercedes","Vinfast", "Tesla"])
    else:
        return redirect(url_for("login"))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/logout')
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))

@app.route('/login', methods=["GET","POST"])
def login():
    if "user" in session:
        return redirect(url_for("user"))
    if request.method == "POST":
        user_name = request.form["name"]
        session.permanent = True
        if user_name:
            session["user"] = user_name
            return redirect(url_for("user", name= user_name))
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)