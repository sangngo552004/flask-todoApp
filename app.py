from flask_login import logout_user, current_user

from todoList import create_app
from flask import session, request, redirect, url_for, flash

app = create_app()
@app.before_request
def check_session_expiration():
    if "user" not in session and request.endpoint != 'user.login':
        flash("Session expired, please login again!!", category="error")
        logout_user()
        return redirect(url_for("user.login"))


if __name__ == "__main__":
    app.run(debug = True)