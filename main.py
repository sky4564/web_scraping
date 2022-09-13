from flask import Flask
from flask import render_template

app = Flask('job scrapper')

@app.route("/")
def home():
    return "hello world"

@app.route("/hello")
def hello():
    return render_template("home.html", name = "kaki")

app.run("0.0.0.0")

# from extractors.wwr import extract_wwr_jobs
# from extractors.file import save_to_file

# keyword = input("what do u want search ???")

# jobs = extract_wwr_jobs(keyword)

# save_to_file(keyword, jobs)

 