from flask import Flask, jsonify, request, render_template
import random

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)


## Your code goes here! ##


@app.route('/')
def login():
    return render_template("home.html", year="2021")


## And doesn't go after this line. ##

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(  # Starts the site
        host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
        port=random.randint(2000, 9000),  # Randomly select the port the machine hosts on.
        debug=True
    )