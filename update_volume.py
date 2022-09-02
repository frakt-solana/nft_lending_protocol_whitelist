import json
import os
import time
import requests

now = int(time.time())

API_KEY = ""
wl = json.load(open("whitelist.json"))

from collections import namedtuple
Response = namedtuple('Response', ['status_code'])

counter_it = 0
for i in wl:

  url = "https://beta.api.solanalysis.com/rest/get-project-stat-hist"
  if not i['hyperspaceSlug']:
    print(i['name'])
    continue

  payload = json.dumps({
    "conditions": {
      "project_ids": [
        i['hyperspaceSlug']
      ],
      "start_timestamp": now - 86400*7,
      "end_timestamp": now,
      "time_granularity": "PER_DAY"
    },
    "pagination_info": {
      "page_number": 1,
      "page_size": 10
    }
  })
  headers = {
    'Authorization': API_KEY,
    'Content-Type': 'application/json'
  }
  response = Response(500)
  counter = 0
  while response.status_code != 200:
    response = requests.request("POST", url, headers=headers, data=payload)
    time.sleep(5)
    counter += 1
    if counter > 30:
      print(i['hyperspaceSlug'])
      print(i['name'])
      break
    if response.status_code != 200 :
      print(response)
      print(i['hyperspaceSlug'])
  volume = 0
  for j in response.json()['project_stat_hist_entries']:
    volume += j['volume']
  i['volume7d'] = volume
  if i['tier'] == 1:
    i['volume_with_tiers'] = i['volume7d'] * 1.25
  elif i['tier'] == 2:
    i['volume_with_tiers'] = i['volume7d'] * 0.7
  else:
    i['volume_with_tiers'] = i['volume7d'] * 0.3
  if counter_it % 10 == 0:
    print(counter_it)
  counter_it += 1

with open("whitelist.json", "w") as file:
    json.dump(wl, file, indent = 1)
