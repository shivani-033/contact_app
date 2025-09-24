from flask import Flask , render_template , redirect , request, url_for
from .import db
from .forms import ContactForm
from .models import ContactList 


def register_routes(app):
    @app.route("/")
    def home():
        contacts = ContactList.query.all()
        return render_template("index.html" , contacts = contacts)
    
    @app.route("/add" , methods = ["POST" , "GET"])
    def add_contact():
        form = ContactForm()
        if form.validate_on_submit():
            new_contact = ContactList(
            name=form.name.data,
            phone=form.phone.data,
            email=form.email.data
            )
            db.session.add(new_contact)
            db.session.commit()

            # db.session.commit()
            return redirect(url_for("home"))
        return render_template("add_contact.html" , form = form)