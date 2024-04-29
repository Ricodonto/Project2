# request is used to handle requests and forms
# session allows us to store session data throughout the website
from flask import Blueprint, render_template, url_for, redirect, request, session

import pypyodbc as odbc
# 'ODBC Driver 17 for SQL Server'
# 'SQL SERVER'
DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
SERVER_NAME = r'LAPTOP-KICEGSLT\SQLEXPRESS01'
DATABASE_NAME = 'carpooling'

# uid=<username>;
# pwd=<password>;

routes = Blueprint( __name__, "routes", static_folder="static", template_folder="templates")


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
        return redirect(url_for("routes.test1"))
    else:
        if 'user' in session:
            return redirect(url_for("routes.user"))
        return render_template("login.html")

@routes.route('/test1')
def test1():
    cnxn_str = session['cnxn_str']
    conn = odbc.connect(cnxn_str, autocommit=True)
    cursor = conn.cursor()
    SQL_STATEMENT = """
    select * from officials
    """

    cursor.execute(SQL_STATEMENT)
    rows = cursor.fetchall()

    for row in rows:
        print(row[1])
        
    return render_template("table.html", rows=rows)



@routes.route('/')
def test():
    return render_template("table.html")

# The name of the parameter in the def function should be the same as the name in the <>
@routes.route('/user')
def user():
    if "user" in session:
        return session['user']
    else:
        return redirect(url_for('routes.login'))

@routes.route('/about')
def about():
    return "This is the about page"

@routes.route('/logout')
def logout():
    session.pop("user", None)
    return "session cleared"

@routes.route('/disconnect')
def disc():
    session.pop("cnxn_str", None)
    return "database has been disconnected"

# @routes.route('/home')
# def home():
#     return "Welcome to the homepage"

# # render_template takes in the name of the html file in the templates folder
# # surrounding the url with two slashes allows the user to access that route with or without an ending /
# @routes.route('/')
# def landing():
#     # If you want to pass a value from python to the html template you need to add a parameter with the name of that value in the html document, and assign the value to it
#     return render_template("test.html", content="hello", number=2)

# @routes.route('/<username>')
# def user(username):
#     return f"{username}"

# # url_for takes a string of the name of the function you want to direct to and the other arguments are the parameters you would pass to that function
# @routes.route('/wrong')
# def wrong():
#     return redirect(url_for("user", username="Rico"))
