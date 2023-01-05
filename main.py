from flask import Flask, render_template

app = Flask("Job Scraper")

@app.route("/")
def home():
    return render_template("home.html", name = "WS K")

app.run("127.0.0.1")
