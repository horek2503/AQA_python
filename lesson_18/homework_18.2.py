import requests
import os

server_url = 'http://127.0.0.1:8080'
image_file_name = 'cat.jpg'


def upload_image_to_server(filename):
    post_url = f"{server_url}/upload"

    with open(filename, mode='rb') as file:
        file_to_upload = {
            "image": file.read()
        }

    response = requests.post(url=post_url, files=file_to_upload)
    return os.path.basename(response.json()['image_url'])


def get_image_url_from_server(filename):
    get_url = f"{server_url}/image/{filename}"
    headers = {
        'Content-Type': 'text'
    }

    response = requests.get(url=get_url, headers=headers)
    return response.json()['image_url']


def delete_image_from_server(filename):
    delete_url = f"{server_url}/delete/{filename}"
    response = requests.delete(delete_url)
    print(response.json())


uploaded_image_filename = upload_image_to_server(image_file_name)

uploaded_image_url = get_image_url_from_server(uploaded_image_filename)

delete_image_from_server(uploaded_image_filename)
