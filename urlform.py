from flask import Flask, render_template, request, redirect
from scrape import scraper as scraper
app = Flask(__name__)

lst = []

@app.route('/')
def hello_world():
    author = "Me"
    name = "You"
    return render_template('index.html', author=author, name=name)


@app.route('/signup', methods = ['POST'])
def signup():
    url = request.form['URL']
    #throws unknown url type error
    scraper(url)
    return redirect('/')

@app.route('/emails.html')
def emails():
    return render_template('urls.html', email_addresses=email_addresses)

if __name__ == "__main__":
    app.run()

 

