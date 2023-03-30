import os
from urllib import parse

import requests


def get_files_ext(pic_url):
    split_url = parse.urlparse(parse.unquote(pic_url))
    file_name = os.path.split(split_url[2])[1]
    ext = os.path.splitext(file_name)[1]
    return ext


def load_photo_from_internet(url, filename, path, payload=None):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    file_format = get_files_ext(url)

    if not os.path.exists(path):
        os.mkdir(path)

    image_path = os.path.join(path, (f'{filename}{file_format}'))
    with open(image_path, 'wb') as file:
        file.write(response.content)
