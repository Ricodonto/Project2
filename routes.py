from flask import Blueprint, render_template, url_for, redirect


routes = Blueprint( __name__, "routes", static_folder="static", template_folder="templates")


@routes.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@routes.route('/')
def test():
    return render_template("table.html")

@routes.route('/about')
def about():
    return "This is the about page"

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
