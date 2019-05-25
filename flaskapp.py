#https://codepen.io/sahil4test/pen/xERYvX

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

#if it is run directly with python, run in debug mode
if __name__ == '__main__':
    app.run(debug=True)


#this is where the functionality goes for categorization.
    