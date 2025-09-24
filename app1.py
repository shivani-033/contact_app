from contact_app import create_app
from flask import Flask

app = create_app()

app.run(debug=True)