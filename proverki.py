from datetime import datetime, date, timedelta
import requests
import json
from settings_tb import SiteSettings

d = date.today()
next_day = d + timedelta(days=1)

date_now = date.today()
day_now = date.today().day
month_now = date.today().month
year_now = date.today().year
date_next = date_now + timedelta(days=1)
dey_next = date_next.day
month_next = date_next.month
year_next = date_next.year


# print(day_now)
# print(month_now)
# print(year_now)
# print(dey_next)
# print(month_next)
# print(year_next)

# headers = {
#     "content-type": "application/json",
#     "X-RapidAPI-Key": "0aed662dfdmshe2b53181f0561acp19edabjsndb7e912c651d",
#     "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
# }
#
# payload = {"destination": {"regionId": "3000"}}
#
# payload2 = {
#
#     "destination": {"regionId": "3000"},
#
#     "resultsStartingIndex": 0,
#     "resultsSize": 200,
#     "sort": "PRICE_LOW_TO_HIGH"}
#
# payload3 = {'currency': 'USD',
#            'eapid': 1,
#            'locale': 'ru_RU',
#            'siteId': 300000001,
#            'destination': {
#                'regionId': '3000' # id из первого запроса
#            },
#            'checkInDate': {'day': 7, 'month': 12, 'year': 2022},
#            'checkOutDate': {'day': 9, 'month': 12, 'year': 2022},
#            'rooms': [{'adults': 1}],
#            'resultsStartingIndex': 0,
#            'resultsSize': 10,
#            'sort': 'PRICE_LOW_TO_HIGH',
#            'filters': {'availableFilter': 'SHOW_AVAILABLE_ONLY'}
#            }
#
#
# # response = requests.post(url, json=payload, headers=headers)
#
#
# url = 'https://hotels4.p.rapidapi.com/properties/v2/list'
#
# hotel_response = requests.request('POST', url, headers=headers, data=payload3, timeout=50)
#
# print(hotel_response)

def search_element(data, tag):
    result = None
    if tag in data:
        return data[tag]
    for key, value in data.items():
        if isinstance(value, list):
            return search_element(value[0], tag)
        if isinstance(value, dict):
            result = search_element(value, tag)
            if result:
                return result
    return result

box = []
with open('test.json', 'r') as file:
    sdf = json.load(file)
    slovar = search_element(sdf, "properties")

    for item in slovar:
        dic_hotels = {'hotel_name': item.get("name"), 'hotel_id': item.get("id"),
                      'hotel_distanse': item.get("destinationInfo").get("distanceFromDestination").get("value"),
                      'hotel_pries_for_nith': item.get("price").get("lead").get("amount")}
        box.append(dic_hotels)
print(box)



    # with open('tsfdf.json', '+w') as edfd:
    #     json.dump(slovar, edfd, indent=4)

