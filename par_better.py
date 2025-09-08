# coding: utf-8
import pandas as pd
score_dist = pd.read_csv("score_dist.csv")
score_dist.head()
score_dist.columns
score_dist.info()
score_dist[["Birdie", "Par"]]).sum
score_dist[["Birdie", "Par"]].sum
score_dist.info()
score_dist[["Name", "Birdie", "Par"]].sum
score_dist[["Name", "Birdie", "Par"]].sum(axis = 1)
score_dist[["Birdie", "Par"]].sum(axis = 1)
score_dist.info()
score_dist = pd.read_csv("score_dist.csv", index_col="Nsme")
score_dist = pd.read_csv("score_dist.csv", index_col="Name")
score_dist.info()
score_dist[["Birdie", "Par"]].sum(axis = 1)
score_dist["par_or_better_percentage"] = score_dist[["Birdie", "Par"]].sum(axis = 1) / score_dist.sum(axis = 1)
score_dist.info()
score_dist['par_or_better_percentage']
