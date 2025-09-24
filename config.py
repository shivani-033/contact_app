import os

class Config:
    SECRET_KEY = 'your_keys'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:yourpassword@localhost/contact_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False