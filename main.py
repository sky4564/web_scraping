from flask import Flask

app = Flask('job scrapper')

@app.route("/")
def home():
    return 'hi there'
    

app.run("0.0.0.0")
    
    








# from extractors.wwr import extract_wwr_jobs
# from extractors.file import save_to_file

# keyword = input("what do u want search ???")

# jobs = extract_wwr_jobs(keyword)

# save_to_file(keyword, jobs)

 