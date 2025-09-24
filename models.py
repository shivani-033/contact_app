from flask import Flask
from contact_app import create_app , db

class ContactList(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(50) , nullable = False)
    phone = db.Column(db.String(15) , nullable = False)
    email = db.Column(db.String(20) , nullable = False)