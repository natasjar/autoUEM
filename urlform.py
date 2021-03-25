from flask import Flask, render_template, request, redirect
import scrape as s
app = Flask(__name__)

lst = []

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/signup', methods = ['POST'])
def signup():
    url = request.form['URL']
    #throws unknown url type error
    s.img_scrape(url)
    return redirect('/')

# @app.route('/emails.html')
# def emails():
#     return render_template('urls.html', email_addresses=email_addresses)

if __name__ == "__main__":
    app.run(port=8080, debug = False)

 

