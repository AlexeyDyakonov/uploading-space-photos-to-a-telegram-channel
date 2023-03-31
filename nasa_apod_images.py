import argparse
import os

import requests
from dotenv import load_dotenv

from load_photo_from_internet import load_photo_from_internet


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
    nasa_photos = response.json()

    for number, image in enumerate(nasa_photos, start=1):
        if image.get('hdurl'):
            load_photo_from_internet(
                image['hdurl'],
                f'nasa_apod_{number}',
                args.path,
                params
            )
