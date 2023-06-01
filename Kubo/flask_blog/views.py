from flask_blog import app


@app.route('/')
def show_enrtries():
    return "Hello World!"
