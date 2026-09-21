import requests
import random

base_url = 'https://images-api.nasa.gov'
search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20
}


def search_nasa_assets(params: dict) -> list:
    search_url = f'{base_url}/search'
    list_of_ids = []
    try:
        data = requests.get(search_url, params=params)
    except Exception as e:
        print(f"Couldn't execute request to {search_url} with params: {params}. Exception is {e}")
    else:
        if data.status_code == 200:
            list_of_items = data.json()['collection']['items']
            if len(list_of_items) > 0:
                for item in list_of_items:
                    current_id = item['data'][0]['nasa_id']
                    list_of_ids.append(current_id)
    return list_of_ids


def save_nasa_asset_image(nasa_id: str, filename: str):
    current_asset_url = f"{base_url}/asset/{nasa_id}"
    image_url = ''

    try:
        current_asset_data = requests.get(current_asset_url)
    except Exception as e:
        print(f"Couldn't get asset data by url {current_asset_url}. Exception occurred - {e}")
    else:
        current_asset_image_urls = current_asset_data.json()['collection']['items']
        for url in current_asset_image_urls:
            # Trying to get at least some image URL
            if url['href'].endswith('.jpg'):
                image_url = url['href']
                # Checking if original URL exists
                if 'orig' in url['href']:
                    image_url = url['href']
                    break

    try:
        image_data = requests.get(image_url)
    except Exception as e:
        print(f"Couldn't get and save image by url {image_url}. Exception occurred - {e}")
    else:
        with open(filename, mode='wb') as file:
            file.write(image_data.content)


asset_ids = search_nasa_assets(search_params)

selected_asset_ids = random.sample(asset_ids, 2)

for asset_id in selected_asset_ids:
    save_nasa_asset_image(nasa_id=asset_id, filename=f'{asset_id}.jpg')
