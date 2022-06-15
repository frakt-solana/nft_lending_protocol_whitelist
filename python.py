import json
tmp = open('whitelist.json')
df = json.load(tmp)
print(len(df))
# for i in range(len(df)):
#     tmp_mints = df[i]['whitelisted_mints']
#     del df[i]['whitelisted_mints']
#     df[i]['time_based_liquidity_pool'] = df[i]['liquidity_pool']
#     df[i]['price_based_liquidity_pool'] = df[i]['liquidity_pool']
#     del df[i]['liquidity_pool']
#     df[i]['whitelisted_mints'] = tmp_mints

with open("whitelist.json", "w") as file:
    json.dump(df, file, indent = 1)
    