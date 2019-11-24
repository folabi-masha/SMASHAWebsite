from flask import Blueprint, render_template, request, redirect

from .extensions import db
from .models import Emails

main = Blueprint('main', __name__)


@main.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        get_email = request.form['email']
        new_email = Emails(emails=get_email)

        try:
            db.session.add(new_email)
            db.session.commit()
            return redirect('/')
        except:
            return render_template("bio.html")

    else:
        return render_template("home.html")


@main.route('/music',  methods=['POST', 'GET'])
def music():
    if request.method == 'POST':
        get_email = request.form['email']
        new_email = Emails(emails=get_email)

        try:
            db.session.add(new_email)
            db.session.commit()
            return redirect('/music')
        except:
            return render_template("bio.html")

    else:
        return render_template("music.html")


@main.route('/contact',  methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        get_email = request.form['email']
        new_email = Emails(emails=get_email)

        try:
            db.session.add(new_email)
            db.session.commit()
            return redirect('/contact')
        except:
            return render_template("bio.html")

    else:
        return render_template("contact.html")
