from collections import namedtuple
from itertools import combinations
from pprint import pprint
import pandas as pd

score_dist = pd.read_csv("score_dist_no_sub.csv", index_col="Name")
score_dist["par_or_better_percentage"] =  score_dist[["Eagle or better", "Birdie", "Par"]].sum(axis = 1) / score_dist.sum(axis = 1)
score_dist['par_or_better_percentage'] = score_dist['par_or_better_percentage'] * 100
player_index = [10.8, 8.9, 7.1, 13.3, 7.1, 13.3, 8.1, 0.2, 21.5, 11.7, 14.7, 11.7, 5.4, 3.9, 11.0, 9.8, 7.9, 16.2, 9.8, 6.0, 6.9, 8.2]
score_dist['HIndex'] = player_index
player_list = list(score_dist.index)
# TODO: make final roster (eliminate subs)

Player = namedtuple("Player", "id name hindex par_or_better")
player_set = set()

for i, p in enumerate(player_list):
    player_set.add(
        Player(i, 
               p, 
               float(score_dist["HIndex"].loc[p]),
               int(score_dist['par_or_better_percentage'].loc[p])
               )
    )

all_teams = []
for team in combinations(player_set, 4):
    all_teams.append(team) 

# INDEX TOTAL FOR EVERY TEAM
team_indices = []
for i, p_tup in enumerate(all_teams):
    index_sum = 0
    for p in p_tup:
        index_sum += p.hindex
    team_indices.append((i, round(index_sum, 2)))
    
print("HANDICAP INDEX SECTION")
sorted_indices = sorted(team_indices, key = lambda x: x[1])
print(sorted_indices[len(sorted_indices) // 2])
n = len(sorted_indices)
print(f"average: {sum(j[1] for j in sorted_indices) / n}")
print(f"length: {n}")
#print(sorted_indices[((n-50)//2):((n+50)//2)])
median_teams = list(filter(lambda x: x[1] == 38.5, sorted_indices))
print(median_teams)
median_teams_idx = [i[0] for i in median_teams]
print(median_teams_idx)
median_team_rosters = [all_teams[i] for i in median_teams_idx]
pprint(median_team_rosters[:10])

# PAR OR BETTER FOR EACH TEAM
team_indices = []
for i, p_tup in enumerate(all_teams):
    par_breaker_sum = 0
    for p in p_tup:
        par_breaker_sum += p.par_or_better
    team_indices.append((i, round(par_breaker_sum, 2)))
    
print("PAR BREAKER SECTION")
sorted_indices = sorted(team_indices, key = lambda x: x[1])
print(sorted_indices[len(sorted_indices) // 2])
n = len(sorted_indices)
print(f"average: {sum(j[1] for j in sorted_indices) / n}")
print(f"length: {n}")
median_teams = list(filter(lambda x: x[1] == 95, sorted_indices))
print(median_teams)
median_teams_idx = [i[0] for i in median_teams]
print(median_teams_idx)
median_team_rosters = [all_teams[i] for i in median_teams_idx]
pprint(median_team_rosters)
print("OK")
