from flask import Flask, render_template, url_for,flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ada85258046a985819107971857c112d'

posts = [
    {
        "author": 'Mustaf Ahmed',
        "title": 'Blog post 1',
        "content": 'First post content',
        "date_posted": "May 20, 2019"
    },
    {
        "author": 'Marta Vidal',
        "title": 'Blog post 2',
        "content": 'Second post content',
        "date_posted": "april 8, 2019  "
    },
     {
        "author": 'Tala Waad',
        "title": 'Blog post 3',
        "content": 'Third post content',
        "date_posted": "april 10, 2019  "
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

@app.route("/register",  methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect('home')
    # return "<h1>About Page!<h1/>"
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    # return "<h1>About Page!<h1/>"
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=true)
