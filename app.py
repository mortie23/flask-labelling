from flask import Flask, request, render_template, current_app
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/category')
def index():
    conn = get_db_connection()
    categories = conn.execute('SELECT * FROM category').fetchall()
    conn.close()
    return render_template('category.html', categories=categories)


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/files')
def files():
    return render_template('files.html')


@app.route('/labelling')
def labelling():
    return render_template('labelling.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(file.filename)
    return f'{file.filename} uploaded successfully'


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5123,
        debug=True
    )
