import os
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

#Create our index or root / route
@app.route("/")
def home():
  return render_template('home.html')

@app.route("/index", methods=["GET", "POST"])
def index():
	notes = [{ "name":"First Note Ever",
            "author":"Abhiram",
            "content":"This text is coming from the content field"
           },
       { "name":"Finish this Blog",
            "author":"Abhiram",
            "content":"Show the template control structures"

       },
       {"name":"Deploy this app to OpenShift",
            "author":"Abhiram",
            "content":"When finished coding this app deploy it to OpenShift"

       }]
	return render_template("index.html",notes=notes)

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == "__main__":
    app.run(debug = "True")