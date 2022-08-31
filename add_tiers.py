import pandas as pd
import json
import os

wl = json.load(open("whitelist.json"))
tiers = pd.read_csv("tiers.csv")
key = "SOLANALYSIS_API_KEY"
value = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJGcmFrdCIsIm5hbWUiOiJIeXBlcnNwYWNlIiwiaWF0IjoxNTE2MjM5MDIyfQ.nj4KiED30rxqWfDHeFJEqUdCOekZu9_yB_y2Y55tXdc"
os.system("{0}={1}".format(key, value))
for i in wl:
    tmp_mints = i['whitelisted_mints']
    del i['whitelisted_mints']
    i['tier'] = int(tiers.loc[tiers['name'] == i['name'], 'tier'].values[0])
    i['volume7d'] = 0
    i['whitelisted_mints'] = tmp_mints


with open("tmp_wl.json", "w") as file:
    json.dump(wl, file, indent = 1)
