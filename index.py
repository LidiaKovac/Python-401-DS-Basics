# my task here will be to analyze a dataset of fake job postings.
# I will analyze salary, industries and required experience

import numpy as np
import pandas as pd

jobs = pd.read_csv("./data/jobs.csv")

# i am going to delete some columns I think are not needed
jobs.drop(columns=["has_questions", "fraudulent",
          "has_company_logo", "company_profile", "description", "benefits", "telecommuting"])
         # title,location,department,salary_range,requirements,has_company_logo,employment_type,required_experience,required_education,industry,function


clean = jobs.dropna()
min = []
max = []
for job in clean["salary_range"]:
    # excludes all "0-0" salaries
    if "-" in job:
        if job.split("-")[0].isdigit():
            min.append(int(job.split("-")[0]))
        if job.split("-")[1].isdigit():
            max.append(int(job.split("-")[1]))
 #the max salary is often what is missing, using this to even out the different lenghts
clean = clean[0:len(min)]
clean["min_salary"] = min
clean = clean[0:len(max)]
clean["max_salary"] = max

usOnly = clean[clean["location"].str.contains("US", case=False)]
 
#print(clean[["title", "industry", "salary_range", "required_experience"]])
print(usOnly[["title","min_salary", "max_salary"]])

#Standard Deviation: how far values are from the mean value 
#Let's do it for both min and max salary 
#steps to calculate: 

#    1. calculate mean 
#    2. for each element in ds, calculate the diff with the mean and square it 
#    3. calculate mean of the (squared) differences
#    4. calculate sqrt of the last mean calculated = standard deviation

#MIN SALARY 

def calc_stndrd_dev (dataset): 
    mean = np.mean(dataset)
    squared_diff = []
    for entry in dataset: 
        squared_diff.append((entry - mean)** 2) 
    sqrd_mean = np.mean(squared_diff)
    return np.sqrt(sqrd_mean)

print(calc_stndrd_dev(usOnly["min_salary"]))
print(calc_stndrd_dev(usOnly["max_salary"]))
