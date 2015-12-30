from flask import Flask, render_template, redirect, url_for
import time
app = Flask(__name__)

@app.route("/") # This is the page's URL
def homepage(): # Function to return the response for the homepage
    #      Renders template  Template filename  Data given to template
    return render_template("homepage.html", time=time.strftime("%c"))

@app.route("/doSomething")
def do_something():
    time.sleep(5)
    return redirect(url_for('homepage'))

# Only do the webserver stuff if we're being run directly from the CLI
if __name__ == "__main__":
    # Allow connections from anyone, listen on port 8091
    # Also enable pretty stack traces
    app.run(host="0.0.0.0", port=8091, debug=True)
