from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        "Author": 'Mustaf Ahmed',
        "Title": 'Blog post 1',
        "content": 'First post content',
        "date_posted": "May 20, 2019"
    },
    {
        "Author": 'Maria Johnson',
        "Title": 'Blog post 2',
        "content": 'Second post content',
        "date_posted": "april 8, 2019  "
    }
]

@app.route("/")
@app.route("/home")
def home():
    # return "<h1>Home Page!<h1/>"
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    # return "<h1>About Page!<h1/>"
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=true)
