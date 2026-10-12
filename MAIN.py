import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("movies.csv")
print(data)
print(data.head(10))
print(data.columns)

data1 = pd.read_csv("ratings.csv")
print(data1)
print(data1.head(10))
print(data1.columns)

data["year"] = data.title.str.extract(r'(\(\d\d\d\d\))',expand = True)
data["year"] = data.year.str.extract(r'(\d\d\d\d)',expand = True)
data["title"] = data.title.str.replace(r'(\(\d\d\d\d\))','',regex = True)
data["title"] = data["title"].apply(lambda x:x.strip())
print(data.head())
data["genres"] = data.genres.str.split("|")
movies = data.copy()
for i, row in data.iterrows():
    for g in row["genres"]:
        movies.at[i,g] = 1
movies = movies.fillna(0)
print(data.head())

data1 = data1.drop(["timestamp"],axis = 1)
print(data1.head())
g = movies.drop(["movieId","title","genres","year"],axis = 1)
count = g.sum().sort_values(ascending=False)
plt.figure(figsize=(10,5))
plt.bar(count.index,count.values,color ="black")
plt.title("MOVIES FOR GENRES")
plt.xlabel("GENRES")
plt.ylabel("NUMBER OF MOVIES")
plt.xticks(rotation=45,ha="right")
plt.tight_layout()
plt.show()