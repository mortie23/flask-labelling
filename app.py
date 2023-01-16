from flask import Flask, request, render_template, current_app
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)


class Labels(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    commentText = db.Column(db.String(100))
    labelML = db.Column(db.String(100))
    labelUser = db.Column(db.String(100))


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/files')
def files():
    return render_template('files.html')


@app.route('/labelling')
def labelling():
    return render_template('labelling.html')


@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(file.filename)
    return f'{file.filename} uploaded successfully'


if __name__ == '__main__':
    app.run(host="0.0.0.0",
            port=5123,
            debug=True)
