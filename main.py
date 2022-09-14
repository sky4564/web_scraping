from extractors.wwr import extract_wwr_jobs
from extractors.file import save_to_file

from flask import Flask, render_template, request



app = Flask('job scrapper')

@app.route("/")
def home():
    return "hello world" 

@app.route("/hello")
def hello():
    return render_template("home.html", name = "kaki")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    jobs = extract_wwr_jobs(keyword)
    save_to_file(keyword, jobs)
    
    return render_template("search.html", keyword = keyword, jobs = jobs)

app.run("0.0.0.0")


# keyword = input("what do u want search ???")



 