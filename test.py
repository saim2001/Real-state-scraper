#

# def address_prs(address):
#     parsed_address = ap.parse_address(address)
#     print(parsed_address.state)

# address_prs('146 EARLSCOURT AVE|Toronto, Ontario M6E4A9')
# # with open('data.json', "r") as json_file:
#     loaded_data = json.load(json_file)



# filtered_data = {}
# for i in loaded_data:
#     postal_type = i['postal_code'][0:2]
#     if postal_type not in filtered_data.keys():
#         filtered_data[postal_type] = [i]
#     else:
#         filtered_data[postal_type].append(i)

# with open('output.json', "w") as json_file:
#     dumped_data = json.dump(filtered_data,json_file)



# with pd.ExcelWriter('output.xlsx', mode='a', engine='openpyxl') as writer:

#     for key,value in filtered_data.items():
#         df = pd.DataFrame(value)
#         df.to_excel(writer, sheet_name=key, index=False)

from datetime import datetime

print(datetime.strptime("2024-05-01", "%Y-%m-%d"))
print(tuple({1:1,2:1}.values()))