# my task here will be to analyze a dataset of fake job postings.
# I will analyze salary, industries and required experience


import numpy as np
import pandas as pd

jobs = pd.read_csv("./data/jobs.csv", sep=",")

# i am going to delete some columns I think are not needed
jobs.drop(columns=["has_questions", "fraudulent",
          "has_company_logo", "company_profile", "description"])

clean = jobs.dropna(subset=["salary_range"])
min = []
max = []
for job in clean["salary_range"]:
    # excludes all "0-0" salaries
    if "-" in job and (job.split("-")[0] != "0" and job.split("-")[1] != "0"):
        min.append(job.split("-")[0])
        max.append(job.split("-")[1])
clean = clean[0:len(max)] #the max salary is often what is missing, using this to even out the different lenghts
clean["min_salary"] = min
clean["max_salary"] = max
print(clean[["title", "industry", "salary_range", "required_experience"]])
print(clean[["min_salary", "max_salary"]])
