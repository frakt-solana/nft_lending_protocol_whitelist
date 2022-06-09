import json
tmp = open('whitelist.json')
df = json.load(tmp)
print(len(df))
# for i in range(len(df)):
#     tmp_mints = df[i]['whitelisted_mints']
#     del df[i]['whitelisted_mints']
#     df[i]['is_trusted_volume'] = False
#     if "banksea_info_post_url" in df[i].keys():
#         pass
#     else:
#         df[i]['banksea_info_post_url'] = None
#     if "hyperspaceSlug" in df[i].keys():
#         pass
#     else:
#         df[i]['hyperspaceSlug'] = None

#     if "max_amount_of_active_loans" in df[i].keys():
#         pass
#     else:
#         df[i]['max_amount_of_active_loans'] = 15
#     df[i]['whitelisted_mints'] = tmp_mints
    # if df[i]['creator'] == "9BKWqDHfHZh9j39xakYVMdr6hXmCLHH5VfCpeq2idU9L":
    #     print(i)

# with open("whitelist.json", "w") as file:
#     json.dump(df, file, indent = 1)
    