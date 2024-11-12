from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/user/<name>')
def hello_world(name):
    return render_template('index.html', content = name, cars = ["BMW","Mercedes","Vinfast", "Tesla"])

if __name__ == "__main__":
    app.run(debug=True)