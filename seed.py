"""Seed file to make sample data for Users db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users
one = User(first='Jarred', last="Baird", image_url="https://static2.cbrimages.com/wordpress/wp-content/uploads/2020/06/Screenshot-2020-07-04-at-11.57.49-PM.jpg?q=50&fit=crop&w=740&h=370")
two = User(first='Sonic', last="the Hedgehog", image_url="https://static.wikia.nocookie.net/heroes-and-villians/images/2/27/SFModernSonicRender.png/revision/latest/scale-to-width-down/1000?cb=20190408171839")
three = User(first='Butt', last="Farts")
four = User(first='Booty', last="Farts")

# Add new objects to session, so they'll persist
db.session.add(one)
db.session.add(two)
db.session.add(three)
db.session.add(four)

# Commit--otherwise, this never gets saved!
db.session.commit()
