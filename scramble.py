from collections import namedtuple
from itertools import combinations
from pprint import pprint
import pandas as pd

score_dist = pd.read_csv("score_dist_scramble.csv", index_col="Name")
score_dist["par_or_better_percentage"] =  score_dist[["Eagle or better", "Birdie", "Par"]].sum(axis = 1) / score_dist.sum(axis = 1)
score_dist['par_or_better_percentage'] = score_dist['par_or_better_percentage'] * 100
player_list = list(score_dist.index)
score_dist["Total Holes"] = score_dist.drop(["HIndex", "par_or_better_percentage"], axis = 1).sum(axis = 1)
pprint(score_dist[["HIndex", "par_or_better_percentage"]])
pprint(score_dist[["Eagle or better", "Birdie", "Par", "Total Holes", "par_or_better_percentage"]].rename(columns = {"par_or_better_percentage": "POB_percentage", "Eagle or better": "Eagle"}))
print("==================================================")
team_str = [
    ['Lederle, Mike', 'Wreford, Nick', 'Leighton, Tim', 'Lederle, Saeha'],
    ['Palmer, Bobby', 'Koenig, Zach', 'ramsey, jim', 'Hojnacki, Max'],
    ['Wreford, Bob', 'Rhodehouse, Jason', 'Borrego, Nick', 'West, Travis'],
    ['Gamble, Tim', 'Cindric, Mike', 'Orsette, Rich', 'Clem, Wally'],
    ['Cunningham, John', 'Taylor, Dorian', 'Roberts, Thomas', 'Orsette, Antony']
]
for team in team_str:
    print(f"TEAM: {"; ".join(team)}")
    print(f"INDEX TOTAL: {round(float(score_dist[['HIndex']].loc[team].sum().iloc[0]), 2)}")
    print(f"PAR BREAKER, TEAM AVERAGE {round(float(score_dist[['par_or_better_percentage']].loc[team].sum().iloc[0]) / 4, 2)}")
    print("--------------------------------------------------")

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
    
#print("HANDICAP INDEX SECTION")
sorted_indices = sorted(team_indices, key = lambda x: x[1])
#print(sorted_indices[len(sorted_indices) // 2])
n = len(sorted_indices)
#print(f"average: {sum(j[1] for j in sorted_indices) / n}")
#print(f"length: {n}")
#print(sorted_indices[((n-50)//2):((n+50)//2)])
#median_teams = list(filter(lambda x: x[1] == 38.5, sorted_indices))
#print(median_teams)
#median_teams_idx = [i[0] for i in median_teams]
#print(median_teams_idx)
#median_team_rosters = [all_teams[i] for i in median_teams_idx]
#pprint(median_team_rosters[:10])

# PAR OR BETTER FOR EACH TEAM
team_indices = []
for i, p_tup in enumerate(all_teams):
    par_breaker_sum = 0
    for p in p_tup:
        par_breaker_sum += p.par_or_better
    team_indices.append((i, round(par_breaker_sum, 2)))
    
#print("PAR BREAKER SECTION")
sorted_indices = sorted(team_indices, key = lambda x: x[1])
#print(sorted_indices[len(sorted_indices) // 2])
n = len(sorted_indices)
#print(f"average: {sum(j[1] for j in sorted_indices) / n}")
#print(f"length: {n}")
#median_teams = list(filter(lambda x: x[1] == 95, sorted_indices))
#print(median_teams)
#median_teams_idx = [i[0] for i in median_teams]
#print(median_teams_idx)
#median_team_rosters = [all_teams[i] for i in median_teams_idx]
#pprint(median_team_rosters)
print("OK")
