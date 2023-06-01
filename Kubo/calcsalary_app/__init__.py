from flask import Flask


app = Flask(__name__)
app.config.from_object('calcsalary_app.config')

import calcsalary_app.views
