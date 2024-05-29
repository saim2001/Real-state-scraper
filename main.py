import requests
from scrapy import Selector
import pprint
import pandas as pd
import json
import datetime
import re
from utils import chk_duplicates
from db import insert_single_prop
from datetime import datetime

def parse_address(address):
    # Regular expression pattern to match the postal code
    postal_code_pattern = r'\b[A-Za-z]\d[A-Za-z]\s*\d[A-Za-z]\d\b'

    # Regular expression pattern to match the city
    city_pattern = r'([^,]+),'

    # Regular expression pattern to match the state
    state_pattern = r',\s*([A-Za-z\s]+)'

    # Search for postal code
    postal_code_match = re.search(postal_code_pattern, address)
    postal_code = postal_code_match.group() if postal_code_match else None

    # Search for city
    city_match = re.search(city_pattern, address)
    city = city_match.group(1).strip() if city_match else None

    # Search for state
    state_match = re.search(state_pattern, address)
    state = state_match.group(1).strip() if state_match else None

    return city, state, postal_code


url = "https://api2.realtor.ca/Listing.svc/PropertySearch_Post"

# payload = "CurrentPage=54&Sort=1-D&GeoIds=g30_dpz89rm7&PropertyTypeGroupID=1&TransactionTypeId=2&PropertySearchTypeId=1&Currency=CAD&IncludeHiddenListings=true&RecordsPerPage=48&ApplicationId=1&CultureId=1&Version=7.0"
payload = "ZoomLevel=12&LatitudeMax=43.74933&LongitudeMax=-79.42181&LatitudeMin=43.59089&LongitudeMin=-79.73389&Sort=6-D&GeoIds=g30_dpz89rm7&PropertyTypeGroupID=1&PropertySearchTypeId=1&Currency=CAD&IncludeHiddenListings=false&RecordsPerPage=60&ApplicationId=1&CultureId=1&Version=7.0&CurrentPage=29"
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'cookie': 'visid_incap_2269415=V9C/tNUjR8qr6jZ6IRkZ13qBMGYAAAAAQUIPAAAAAACcZwzOhbA3/FSDh9R4ZmBP; incap_ses_540_2269415=jmFJSswE3X4wcvg3L3d+B32BMGYAAAAA47Dqg912rTvhRpVWdK/LMg==; _gcl_au=1.1.1384782094.1714454913; _gid=GA1.2.640438858.1714454914; visid_incap_3057435=1QzW7BqdTXGaBb1ig+D0X4SBMGYAAAAAQUIPAAAAAAAGdjqcnHbplnWsOHZhL/fd; nlbi_3057435=XuFORKM++zNpMhJboWGLxgAAAACV1plzUaUJqIKkYMwTylZO; incap_ses_1787_3057435=vjOZF2nWRThGudXkDLPMGIWBMGYAAAAA6+u5KcefTR6OumfJpnPubA==; gig_bootstrap_3_mrQiIl6ov44s2X3j6NGWVZ9SDDtplqV7WgdcyEpGYnYxl7ygDWPQHqQqtpSiUfko=gigya-pr_ver4; visid_incap_2271082=s+MPDZX9Q/61WM09u6tw2Q2CMGYAAAAAQUIPAAAAAAAIPlIqYeh5wTJFdAwyfL2U; nlbi_2271082=7ZOLFXOvGkwDutXSVPrQ3QAAAABs6Futfsyn8dsYZnwnn9DS; incap_ses_1787_2271082=dBv7BWovKDaG39jlDLPMGLC1MGYAAAAApXGj0vKLm0vxqcd45ZWAYg==; incap_ses_1293_2269415=XwnCD7GI3zY8X489rajxEcy1MGYAAAAA0euOKbS50yBVitKV3XsMZw==; incap_ses_1787_2269415=CmGjFV6cOR7BqI7mDLPMGKrbMGYAAAAAJ2zIl9eIJ8rDqqVEzgtQ3Q==; reese84=3:xZ4EYMT9EHMDxaj/GoxkWg==:Ms+HCAFb6jU2PnwPEg6AMUKsTgRTFwEbyClfejlNgphou+U97rLvMoWJQl9lzi2lE4Ngc8yvdgm/oqM1rILDNvj2I7NnPrEIXkDaGkMUH13kLi1Mw+Gz6FhTNBW/ucK/i7u6lw2jNtupJmEwo4oalBRB9Lr2wKU/0t9YeKvNFuQkZ7XZl+X36NGNVw8VNmwmrNPyZtJeF/7hjPJLY+R92SWIrOdt1tLy+ZXCCOJjLJrKbDZ7lteO5kHn83+LHZkGsKk2ErLydhiD6BimBxyiqze36Ri9vsGwFKKxau0MpQQG5TC/8ZJePEsN7ybbkVS2i4O1+i8IyvxqAcSSlg7LhSgzZX4hbmYl2qbTrCLdhFtC47sOowtMLw3xJINdEU5ACh6tPVossgj7Y3QVuMTe1h/kfkDRqecjm5EXTAV6TnVxgX1wwzAQEKtg7aWnfoUvNZu0ZsouAuTxKtcj9sFilA==:K/1od7BANUKNz0cwfJBSjKma57ZsY2tHTH/3eE8er14=; _ga_Y07J3B53QP=GS1.1.1714479684.3.1.1714479995.51.0.0; _ga=GA1.2.1394628843.1714454914; incap_ses_1787_2271082=vR/ZQzUvDW+c8rTmDLPMGKrkMGYAAAAA40s8oD8pq+q3aZmxndMq5g==',
  'origin': 'https://www.realtor.ca',
  'priority': 'u=1, i',
  'referer': 'https://www.realtor.ca/',
  'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
}
def scrape_and_filter(filtered_data):
    print(f'->Requesting URL {url}')
    response = requests.request("POST", url, headers=headers, data=payload)
    print(f'->{response.status_code}')

    dict_response = json.loads(response.text)

    date = datetime.now().date()

    unfiltered_data = []
    print(f'results fetched {len(dict_response['Results'])}')
    for i in dict_response['Results']:
        pprint.pprint(i)
        try:
            agent = i['Individual'][0]['Name']
        except:
            try:
                agent = i['Individual'][1]['Name']
            except:
                agent = None
        broker = i['Individual'][0]['Organization']['Name']
        try:
            price = i['Property']['Price']
        except:
            price = f"LeaseRent: {i['Property']['LeaseRent']}"
        address = i['Property']['Address']['AddressText']
        longitude = i['Property']['Address']['Longitude']
        latitude = i['Property']['Address']['Latitude']
        city, state, postal_code = parse_address(address)
        # except Exception as e :
        #     print(e)
        row = {
            'date' : str(date),
            'address' : address,
            'city' : city.replace('\n','').split('|')[-1] if city else None,
            'state' : state.replace('\n','').split(' ')[0] if state else None,
            'postal_code' : postal_code,
            'agent' : agent,
            'broker' : broker,
            'price' : price,
            'longitude' : longitude,
            'latitude' : latitude
            
        }
        unfiltered_data.append(row)
    print('-> Filtering data')

    for i in unfiltered_data:

        if i['postal_code']==None:
            i['address'] = None
        i['date'] = datetime.strptime(i['date'], "%Y-%m-%d")
        i['longitude']  = str(i['longitude'])
        i['latitude']  = str(i['latitude'])   
        duplicate = insert_single_prop(tuple(i.values()))

        if duplicate == 0:
            i['date'] = str(i['date'])
            if i['postal_code']:
                postal_type = i['postal_code'][0:2]
                if postal_type not in filtered_data.keys():
                    filtered_data[postal_type] = [i]
                else:
                    filtered_data[postal_type].append(i)
            else:
                if 'Address not found' in filtered_data.keys():
                    filtered_data['Address not found'].append(i)
                else:
                    filtered_data['Address not found'] = [i]
        else:
            pass
            
        
    i=0
    for key,value in filtered_data.items():
        i = i+len(value)
    print(i)
    return filtered_data


def open_read():
    try:
        with open('output.json', "r") as json_file:
            filtered_data = json.load(json_file)
            return filtered_data
    except FileNotFoundError:
        filtered_data = {} 
        return filtered_data






def dump_file(filtered_data):

    with open('output.json', "w") as json_file:
        dumped_data = json.dump(filtered_data,json_file)

def write_exl_file(filtered_data):
    print('->Writing excel file')
    with pd.ExcelWriter('output.xlsx', mode='a', engine='openpyxl') as writer:

        for key,value in filtered_data.items():
            df = pd.DataFrame(value)
            df.to_excel(writer, sheet_name=key, index=False)
data = open_read()

# filt_data = scrape_and_filter(data)
# dump_file(filt_data)

write_exl_file(data)












