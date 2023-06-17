"""Самый главный управляющий файл"""
import json
import requests
from settings_tb import SiteSettings
from data_base.core_db import crud
from site_api.core_site_api import site_api, url, headers
site = SiteSettings()


db_write = crud.create()
db_read = crud.retrive()

get_m_date = site_api.get_meta_date()
locations = site_api.locacations()




response = get_m_date('GET', url, headers, params=None, timeout=5)
response = response.json()

response_2 = locations('GET', url, headers, params=None, timeout=5)
response_2 = response_2.json()
print(response_2)


# import requests
# import json
# from settings import SiteSettings
#
# site = SiteSettings()
#
# # v2/get-meta-data
# url = "https://hotels4.p.rapidapi.com/v2/get-meta-data"
#
# headers = {
#     "X-RapidAPI-Key": site.api_key.get_secret_value(),
#     "X-RapidAPI-Host": site.api_host
# }  # эти данные лежат в .env а настройки к ним лежат в settings
#
# # response = requests.get(url, headers=headers)
# response_1 = requests.request('GET', url, headers=headers)
# # locations/v3/search
url = "https://hotels4.p.rapidapi.com/locations/v3/search"
#
# querystring = {"q": "new york", "locale": "en_US", "langid": "1033", "siteid": "300000001"}
#
# headers = {
#     "X-RapidAPI-Key": site.api_key.get_secret_value(),
#     "X-RapidAPI-Host": site.api_host
# }
#
# # response = requests.get(url, headers=headers, params=querystring)
# response_2 = requests.request('GET', url, headers=headers, params=querystring)
