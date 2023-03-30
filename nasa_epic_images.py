import argparse
import os

import requests
from dotenv import load_dotenv

from load_photo_from_internet import load_photo_from_internet

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Программа загружает фото Земли сделанные NASA'
    )
    parser.add_argument(
        '-p',
        '--path',
        type=str,
        default='images',
        help='Путь сохранения файлов. Стандартно - папка images'
    )
    args = parser.parse_args()

    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']

    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {'api_key': nasa_api_key}

    response = requests.get(url, params=params)
    response.raise_for_status()
    images_nasa = response.json()

    for index, picture in enumerate(images_nasa):
        picture_name = f"{picture['image']}.png"
        picture_datetime = picture['date']
        picture_date = picture_datetime.split()[0].split('-')
        year, month, day = picture_date
        day, month, year = day, month, year
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{str(year)}/" \
                    f"{str(month)}/{str(day)}/png/{picture_name}"
        load_photo_from_internet(
            image_url,
            f'EPIC_{index}',
            'images',
            params
        )
