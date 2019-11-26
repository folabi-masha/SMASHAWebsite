from flask import Blueprint, render_template, request, redirect

from .extensions import db
from .models import Emails
import re

main = Blueprint('main', __name__)

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


@main.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        get_email = request.form['email']
        new_email = Emails(emails=get_email)

        if(re.search(regex, get_email)):
            try:
                db.session.add(new_email)
                db.session.commit()
                return redirect("/email_added")
            except:
                return render_template("bio.html")
        else:
            return render_template("bio2.html")
    else:
        return render_template("home.html")


@main.route('/music')
def music():
   return render_template("music.html")


@main.route('/contact')
def contact():
    return render_template("contact.html")

@main.route('/email_added', methods=['POST', 'GET'])
def email_added():
    return render_template("email_added.html")
