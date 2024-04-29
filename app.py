# Redict and url_for are used hand in hand to redirect a user from one page to another
# render_template allows a flask to return a html document for a webpage
from flask import Flask, redirect, url_for, render_template
from routes import routes
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.register_blueprint(routes, url_prefix="")
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")



if __name__ == '__main__':
    app.run(debug=True)