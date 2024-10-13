# request is used to handle requests and forms
# session allows us to store session data throughout the website
from flask import Blueprint, render_template, url_for, redirect, request, session

import pypyodbc as odbc
# 'ODBC Driver 17 for SQL Server'
# 'SQL SERVER'
DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
SERVER_NAME = r'DESKTOP-5IS51HK'
DATABASE_NAME = 'carpooling'

# uid=<username>;
# pwd=<password>;

routes = Blueprint( __name__, "routes", static_folder="static", template_folder="templates")


@routes.route('/')
def landing():
    if "user" in session:
        return render_template("landing.html")
    else:
        return redirect(url_for("routes.login"))

@routes.route('/login', methods=['GET', 'POST'])
def login():
    errors = []
    if request.method == "POST":
        username: str=request.form['username']
        password: str=request.form['password']

        session['cnxn_str'] = f"""
            DRIVER={{{DRIVER_NAME}}};
            SERVER={SERVER_NAME};
            DATABASE={DATABASE_NAME};
            Trust_Connection=yes;
            uid={username};
            pwd={password};
        """
        try:
            odbc.connect(session['cnxn_str'], autocommit=True)

        except odbc.DatabaseError:
            errors.append("Login information was incorrect")
            return render_template("login.html", errors=errors)

        print(session['cnxn_str'])
        session['user'] = username
        return redirect(url_for("routes.landing"))
    else:
        if 'user' in session:
            return redirect(url_for("routes.landing"))
        return render_template("login.html")


@routes.route('/logout')
def logout():
    session.pop("user", None)
    return render_template("logout.html")

@routes.route('/disconnect')
def disc():
    session.pop("cnxn_str", None)
    return "database has been disconnected"


