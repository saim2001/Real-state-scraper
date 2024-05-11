
import requests
import json
import pandas
import pprint
import time
import random






sleep_times = [3,4,5,6,7,8]

df = pandas.read_csv('pk.csv')
cities_list = df['city'].to_list()



def generate_payload(payload,city,page):
        print(city)
        payload['organization_locations'] = [city]
        payload['page'] = page
        pprint.pprint(payload)
        return json.dumps(payload)

url = "https://app.apollo.io/api/v1/mixed_companies/search"


payload = {
                "finder_table_layout_id": None,
                "finder_view_id": "5b6dfc5a73f47568b2e5f11c",
                "organization_industry_tag_ids": [
                    "5567e8bb7369641a658f0000"
                ],
                "display_mode": "explorer_mode",
                "per_page": 25,
                "open_factor_names": [],
                "num_fetch_result": 2,
                "context": "companies-index-page",
                "show_suggestions": False,
                "ui_finder_random_seed": "ynu0wtk01ap",
                "cacheKey": 1714806015437
            }

headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/json',
  'cookie': 'mutiny.user.token=4231e4e4-6e6d-4416-ac0e-39d208c7096e; mutiny.user.session=e9916a7b-df18-417c-9c72-87359b0cecd4; mutiny.user.session_number=1; zp__initial_referrer=https://www.google.com/; zp__utm_source=www.google.com; zp__initial_utm_source=www.google.com; __hstc=21978340.07c7f2c94f2a41d43dea274b42148015.1714805799114.1714805799114.1714805799114.1; hubspotutk=07c7f2c94f2a41d43dea274b42148015; __hssrc=1; __q_state_xnwV464CUjypYUw2=eyJ1dWlkIjoiMmJiNDEyMjctZDUxNS00YWFhLTk5ZmItNjU5ZThkYjlkMDU4IiwiY29va2llRG9tYWluIjoiYXBvbGxvLmlvIn0=; GCLB=CL-Tz5K6oe3huwEQAw; _clck=1qsuitl%7C2%7Cflh%7C0%7C1585; _cioanonid=42d7cd99-8182-1e34-64fc-9c7268622267; ZP_Pricing_Split_Test_Variant=23Q2_EC_W49; remember_token_leadgenie_v2=eyJfcmFpbHMiOnsibWVzc2FnZSI6IklqWTBaVEZsTXpCall6TXhNRGt6TURCaE0yTmtNVGt6TUY5c1pXRmtaMlZ1YVdWamIyOXJhV1ZvWVhOb0lnPT0iLCJleHAiOiIyMDI0LTA2LTA0VDA2OjU3OjM2Ljg0OFoiLCJwdXIiOiJjb29raWUucmVtZW1iZXJfdG9rZW5fbGVhZGdlbmllX3YyIn19--aaa661bfb06a4b36a51c3450ce72d96c25855ad6; __hssc=21978340.3.1714805799114; ZP_LATEST_LOGIN_PRICING_VARIANT=23Q2_EC_W49; _clsk=4iivz9%7C1714805859322%7C2%7C1%7Cw.clarity.ms%2Fcollect; _cioid=64e1e30cc3109300a3cd1930; intercom-device-id-dyws6i9m=c3fb624b-6d02-41ae-b728-faaf0f0ddb0e; __stripe_mid=0799bfb7-eb33-410d-928b-38b87198bc7e17f43a; __stripe_sid=8483d8cc-48fc-413a-92bb-563602a304c5fa38c8; intercom-session-dyws6i9m=TGZ0ZDdvUnRudlhMTy8za3QzQk9NU1A3QVhndG94enNCb3gxM0JmTzYrOWN5UWR3SWdFbmRuS1VEUjBHb1Y3QS0tVDdZYnV5OFFXQURyZ3hYdXZjU0grZz09--811332d1935ad7ed043949aa1f660878522e1f6e; amplitude_id_122a93c7d9753d2fe678deffe8fac4cfapollo.io=eyJkZXZpY2VJZCI6IjQyNzQ5NjQxLWExOTItNDMwNS05OGEzLTY4NDgxNmQ1NTBmM1IiLCJ1c2VySWQiOiI2NGUxZTMwY2MzMTA5MzAwYTNjZDE5MzAiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE3MTQ4MDU3OTg1OTAsImxhc3RFdmVudFRpbWUiOjE3MTQ4MDYwMDkzOTIsImV2ZW50SWQiOjgsImlkZW50aWZ5SWQiOjgsInNlcXVlbmNlTnVtYmVyIjoxNn0=; X-CSRF-TOKEN=ZB2WVCQYjVuFZZqY_j7Va6TGP-Djmwzyy8FTYh3coCtbW5fWRt0JJhssixCB3VQz76_dSYYb3c4NCRntCe3dzw; _leadgenie_session=6PqV672L%2BH2%2FB%2BX1RIc2spyvw82RRWNis1LkDzJgfB4oDAMQ%2FBpD%2Bu4dta4zvsrc45Y%2BsLOsEyh808NlY84P1lMxvHCTXlPcxH2QojgypihCXnVAu9cebkVOxiz9iq%2Bau1utqg2T4klr199HbIzk3nfS22%2B0qqT6FMy55OHIwq14Ha0p8pXsEulsZQjzNm8HN2kRMSdhLD6hYlY1wiXbAUIFgZknDcdnieEdT%2BfYr0cmxESj%2FuxagQrmftjkYjQO4H4Yz%2Bpi%2BYHJIeu%2FwNI0eY9CMOpjMy%2BjDew%3D--uTuhqVQzxtMJNIAl--Mg1R%2FJpz6IDEMaNZs5LbEA%3D%3D; _dd_s=rum=0&expire=1714806915394; X-CSRF-TOKEN=oh-fTbPSYtz6z1XVIrGGpVUiA6ay-LnDMwOGLb_o-ledWZ7P0RfmoWSGRF1dUgf9HkvhD9d4aP_1y8yiq9mHsw; _leadgenie_session=yS7CkVJlbFaapCUJa5X5W1huSIAFLofbfG9J2dVUV549X1rpz9WQVBjlF1%2FfRJeQWOuGkkJXPKFrPCZOyqPwCzN%2BceFEuTsMQf8lwSwTg598LBaXDhjKeTFmOLPXuPJk7QScqsQCLs3qMsz%2Fm%2FsT2h6nSqf%2B0U0n7LOJoknlm1TyNXiaJC%2BgZaRLAxQ4jJbCVYrbU%2FVwE4ZEP3kTsOup4lSzt7V7yIlaAYupxPqlQWV1QPDDeNNJdJcrPZWlRZDt2%2BEQdcTIhQ4RWbDu8vayPiQio7lbh1h0ZRo%3D--tYqqaMcFFgLwTods--PuXS0lK2IWScQPoSUabyiw%3D%3D',
  'origin': 'https://app.apollo.io',
  'referer': 'https://app.apollo.io/',
  'sec-ch-ua': '"Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0',
  'x-csrf-token': 'ZB2WVCQYjVuFZZqY_j7Va6TGP-Djmwzyy8FTYh3coCtbW5fWRt0JJhssixCB3VQz76_dSYYb3c4NCRntCe3dzw'
}
response_data = []
for i in cities_list:
    time.sleep(random.choice(sleep_times))
    for j in range(1,6):
        payload_for_request = payload.copy()
        response = requests.request("POST", url, headers=headers, data=generate_payload(payload_for_request,i,j))
        # pprint.pprint(response.text)
        prsed_data = json.loads(response.text)
        for k in prsed_data['organizations']:
             response_data.append({
                'id' : k['id'],
                "name": k['name'],
                "website_url": k['website_url'],
                "blog_url": k['blog_url'],
                "angellist_url": k['angellist_url'],
                "linkedin_url": k['linkedin_url'],
                "twitter_url": k['twitter_url'],
                "facebook_url": k['facebook_url'],
                "primary_phone": k['primary_phone'],
                "phone": k['phone'],
                "founded_year": k['founded_year'],
                "logo_url": k['logo_url'],
                "crunchbase_url": k['crunchbase_url'],
                "primary_domain": k['primary_domain'],
                "owned_by_organization_id": k['owned_by_organization_id']
                })
        time.sleep(random.choice(sleep_times))


df = pandas.DataFrame(response_data)
df.to_csv('output.csv',index=False)

