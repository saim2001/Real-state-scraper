import requests

url = "https://api2.realtor.ca/Listing.svc/PropertySearch_Post"

payload = "CurrentPage=3&Sort=6-D&GeoIds=g30_dpz89rm7&PropertyTypeGroupID=1&TransactionTypeId=2&PropertySearchTypeId=1&Currency=CAD&IncludeHiddenListings=false&RecordsPerPage=12&ApplicationId=1&CultureId=1&Version=7.0"
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

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)