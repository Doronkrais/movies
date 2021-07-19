import pandas as pd
import numpy as np
data = pd.read_csv("data.csv")

years = data["Year"]
new_year = list()
for year in years:
    if int(year) < 1960:
        x="1950-1960"
    elif int(year)>=1960 and int(year) < 1970:
        x="1960-1970"
    elif int(year)>=1970 and int(year)<1980:
        x="1970-1980"
    elif int(year)>=1980 and int(year)<1990:
        x="1980-1990"
    elif int(year)>=1990 and int(year)<2000:
        x="1990-2000"
    elif int(year)>=2000 and int(year)<2010:
        x="2000-2010"
    else:
        x="2010-2022"
    new_year.append(x)
data['Year obj']= new_year
Votes = data["Votes"]
new_Votes = list()

for vote in Votes:
    if vote.find(",") != -1:
        x = vote.split(",", 1)[0]
        y = vote.split(",", 1)[1]
        z = x+y
        if z.find(",") != -1:
            x = z.split(",", 1)[0]
            y = z.split(",", 1)[1]
            z = x + y
    else:
        z = vote
    z = int(z)
    new_Votes.append(z)
data['Votes'] = new_Votes
rating = data["Rating"]
rate1 = list()
for rate in rating:
    if rate < 6.7:
        rate1.append(0)
    else:
        rate1.append(1)
data["label"] = rate1
data.to_csv("data.csv")
