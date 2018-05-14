""" Simple Web-Site using Flask Framework and Bootstrap Styling

    Basic jinja2 template features explored.

"""

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html", css_class="home", header_text="Welcome to my Homepage")

@app.route('/about/')
def about():
    return render_template("about.html", css_class="about", header_text="Curriculum Vitae")

@app.route('/content/')
def content():
    project_list = ["Rocket to go to Jupyter",
                    "Automation system for growing organic food in harsh terrains",
                    "Electro-gravitational transducer, enabling UFO like spacecrafts",
                    "Wireless sensor network for monitoring road traffic, with app to conect to autonomous cars and display map with near vehicles positions"]
    return render_template("content.html", css_class="content", header_text="Interesting Stuff", project_list = project_list)


if __name__=="__main__":
    app.run(debug=True)

