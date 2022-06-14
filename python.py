import json
tmp = open('whitelist.json')
df = json.load(tmp)
print(len(df))
colls_info = {}
for i in range(len(df)):
    if df[i]['collection_info'] in colls_info.keys():
        colls_info[df[i]['collection_info']] += 1
    else:
        colls_info[df[i]['collection_info']] = 1

    # tmp_mints = df[i]['whitelisted_mints']
    # del df[i]['whitelisted_mints']
    # df[i]['is_trusted_volume'] = False
    # if "banksea_info_post_url" in df[i].keys():
    #     pass
    # else:
    #     df[i]['banksea_info_post_url'] = None
    # if "hyperspaceSlug" in df[i].keys():
    #     pass
    # else:
    #     df[i]['hyperspaceSlug'] = None

    # if "tensor_slug" in df[i].keys():
    #     pass
    # else:
    #     df[i]['tensor_slug'] = None

    # if "max_amount_of_active_loans" in df[i].keys():
    #     pass
    # else:
    #     df[i]['max_amount_of_active_loans'] = 15
    # df[i]['whitelisted_mints'] = tmp_mints

# print(set(colls_info.values()))
for i, j in colls_info.items():
    if j == 2:
        print(i)
# with open("whitelist.json", "w") as file:
#     json.dump(df, file, indent = 1)
    