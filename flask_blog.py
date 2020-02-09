from flask import Flask, render_template
app = Flask(__name__)


posts = [
    {
        "author": "Daniel Boadzie",
        "title": "the first",
        "content": "the blog body id smooth",
        "date_created": "April 20, 2019"
    },
    {
        "author": "Sam Wayne",
        "title": "the second",
        "content": "the second blog body id smooth",
        "date_created": "March 20, 2019"
    }
]


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')



if __name__ == '__main__':
    app.run(debug=True)