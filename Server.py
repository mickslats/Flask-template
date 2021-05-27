from flask import Flask, render_template
import datetime

app=Flask(__name__)


@app.route('/')
def home():
    return render_template("Home.html")

@app.route('/about/')
def about():
    return render_template("about.html")


### Copy and past line 11 to line 13 but of course change the bit where it says hoabout and about.htmlif you wish to add anotheer page ##


if __name__=="__main__":
    app.run(debug=True)
