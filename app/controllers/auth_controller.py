from flask import Blueprint, redirect, render_template, request, session, url_for

auth_bp = Blueprint("auth", __name__)

HARDCODED_USERS = {
    "00000": {
        "password": "admin123",
        "name": "Galih A. Pernana",
        "role": "Project Administrator",
    },
}

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if session.get("logged_in"):
        return redirect(url_for("page.dashboard"))

    error = None
    if request.method == "POST":
        nik = request.form.get("nik", "").strip()
        password = request.form.get("password", "").strip()

        user = HARDCODED_USERS.get(nik)
        if user and user["password"] == password:
            session.clear()
            session["logged_in"] = True
            session["nik"] = nik
            session["user_name"] = user["name"]
            session["user_role"] = user["role"]
            return redirect(url_for("page.dashboard"))

        error = "NIK atau Password salah"

    return render_template("pages/login.html", error=error)


@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
