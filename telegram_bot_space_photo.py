import argparse
import os
from random import shuffle
from time import sleep

import telegram
from dotenv import load_dotenv

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Программа загружает фото в заданный телеграм-канал \
        с заданным промежутком'
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
    tg_token = os.environ['TG_TOKEN']
    post_latency = int(os.environ['POST_LATENCY'])
    tg_channel = os.environ['TG_CHANNEL']
    bot = telegram.Bot(token=tg_token)

    dir_name, _, images = next(os.walk(args.path))
    shuffle(images)

    while True:
        for image in images:
            with open(f'{dir_name}/{image}', 'rb') as photo:
                bot.send_photo(chat_id=tg_channel, photo=photo)
            sleep(post_latency)
