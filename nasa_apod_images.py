import argparse
import os

import requests
from dotenv import load_dotenv

from load_photo_from_internet import load_photo_from_internet


def fetch_spacex_last_launch(spacex_url):
    response = requests.get(spacex_url)
    response.raise_for_status()
    pictures_url = response.json()['links']['flickr']['original']
    for picture_index, picture_url in enumerate(pictures_url, start=1):
        load_photo_from_internet(picture_url, f'images/'
                                              f'spacex{picture_index}.jpg')


if __name__ == '__main_':
    parser = argparse.ArgumentParser(
        description='Программа загружает фото дня по версии NASA'
    )
    parser.add_argument(
        '-p',
        '--path',
        type=str,
        default='images',
        help='Путь сохранения файлов. Стандартно - папка images')
    parser.add_argument(
        '-n',
        '--number',
        type=int,
        default=30,
        help='Количество фото. Стандартно - 30'
    )
    args = parser.parse_args()

    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']

    nasa_url = "https://api.nasa.gov/planetary/apod"
    params = {
         "api_key": nasa_api_key,
         "count": args.number,
    }
    response = requests.get(nasa_url, params=params)
    response.raise_for_status()
    images_nasa = response.json()

    for number, image in enumerate(images_nasa, start=1):
        if image.get('hdurl'):
            load_photo_from_internet(
                image['hdurl'],
                f'nasa_apod_{number}',
                args.path,
                params
            )
