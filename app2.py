from flask import Flask, render_template, request, redirect
from peewee import *
from models2 import Post

app = Flask(__name__)

@app.route('/')
def mike():
    all_posts = Post.select()
    return render_template("index.html", posts=all_posts)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        recording = request.form['recording']
        time = request.form['time']

        Post.create(
            name = name,
            recording = recording,
            time = time
        )
        return redirect('/')
    return render_template('create.html')

if __name__ == "__main__":
    app.run(debug=True)