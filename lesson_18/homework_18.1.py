import json
from curlify import to_curl

import requests

base_url = 'https://images-api.nasa.gov'

get_asset_url = f'{base_url}/asset'


def search_nasa_assets(params: dict) -> list:
    search_url = f'{base_url}/search'
    list_of_ids = []
    data = requests.get(search_url, params=params)
    if data.status_code == 200:
        list_of_items = data.json()['collection']['items']
        if len(list_of_items) > 0:
            for item in list_of_items:
                current_id = item['data'][0]['nasa_id']
                list_of_ids.append(current_id)
    return list_of_ids

    # with open('nasa_search_response.json', 'w') as file:
    #     json.dump(data.json(), file, indent = 2)


#
# nasa_id = 'PIA15106'
# img_url = f"{get_asset_url}/{nasa_id}"
# asset_data = requests.get(img_url)
# # print(to_curl(asset_data.request))
# print(asset_data.content)
#
# with open('asset_response.json', mode = 'w') as file:
#     json.dump(asset_data.json(), file, indent = 2)
#
# selected_asset_urls = asset_data.json()['collection']['items']
# for url in selected_asset_urls:
#     if 'orig' in url['href']:
#         print(url['href'])
#
#
search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20
}

asset_ids = search_nasa_assets(search_params)
print(asset_ids)
