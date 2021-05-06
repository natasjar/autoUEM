from flask import Flask, render_template, request, redirect, url_for
import data
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')



@app.route('/signup', methods = ['POST'])
def signup():
    url = request.form['URL']
    email = request.form["email"]

    data.check_info(email, url)
    return render_template('thankyou.html')


if __name__ == "__main__":
    app.run()

 

