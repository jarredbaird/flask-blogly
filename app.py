"""Blogly application."""

from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = 'echnidna_eggs'
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def list_users():
    return redirect('/users')

@app.route('/users')
def display_users():
    users = User.query.all()
    return render_template('list.html', users=users, heading="All Users")

@app.route('/users/<int:id>')
def display_user(id):
    user = User.query.get(id)
    return render_template('details.html', user=user)

@app.route("/users/family/<last>")
def display_family(last):
    family = User.get_users_by_last_name(last)
    return render_template('list.html', users=family, heading=f'The {last} Family')

@app.route('/users/new')
def show_add_user_form():
    return render_template("form.html")

@app.route('/users/edit/<int:id>')
def show_edit_user_form(id):
    user = User.query.get(id)
    return render_template("edit.html", user=user)

@app.route('/users/change/<int:id>', methods=["POST"])
def change_user(id):
    changed_user = User.query.get(id)
    first = request.form['first']
    if first:
        changed_user.first = first
    last = request.form['last']
    if last:
        changed_user.last = last
    image_url = request.form["image_url"]
    if image_url:
        changed_user.image_url = image_url

    db.session.add(changed_user)
    db.session.commit()

    return redirect(f'/users/{changed_user.id}')

@app.route('/users/delete/<int:id>', methods=["POST"])
def delete_user(id):
    deleted_user = User.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect('/users')
    
@app.route('/users/add', methods=["POST"])
def add_user():
    first = request.form['first']
    last = request.form["last"]
    image_url = request.form["image_url"]
    image_url = str(image_url) if image_url else None

    new_user = User(first=first, last=last, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect(f'/users/{new_user.id}')
