import pandas as pd
import json
import os

wl = json.load(open("whitelist.json"))
tiers = pd.read_csv("tiers.csv")
for i in wl:
    tmp_mints = i['whitelisted_mints']
    del i['whitelisted_mints']
    try:
        i['tier'] = int(tiers.loc[tiers['name'] == i['name'], 'tier'].values[0])
    except:
        i['tier'] = 3
    i['volume7d'] = 0
    i['volume_with_tiers'] = 0
    i['whitelisted_mints'] = tmp_mints


with open("whitelist.json", "w") as file:
    json.dump(wl, file, indent = 1)
