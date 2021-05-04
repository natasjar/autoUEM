from flask import Flask, render_template, request, redirect
import scrape as s
import detection as d
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/signup', methods = ['POST'])
def signup():
    url = request.form['URL']
    d.detect_text(s.img_scrape(url))
    return redirect('/')


if __name__ == "__main__":
    app.run()

 

