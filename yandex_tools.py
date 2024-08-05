# сделан базовый функционал, чтобы работало
import yadisk
import os
from config import YANDEX_TOKEN
from yadisk.exceptions import DirectoryExistsError, PathExistsError, PathNotFoundError

async def ya_disk_upload(filename):
    token = YANDEX_TOKEN
    client = yadisk.AsyncClient(token=token)
    async with client:

        # Общая информация о диске
        # print(await client.get_disk_info())
        # params = {
        #     'path': '/test'
        # }
        # folders = requests.put('https://cloud-api.yandex.net/v1/disk/resources', headers=headers, params=params)

        # Смотрим содержимое диска"
        # files = [i async for i in client.listdir("/")]
        try:
            await client.mkdir("/test")
        except DirectoryExistsError:
            print('Folder already exists')

        # Загружает файл на диск
        try:
            await client.upload(os.path.join('./', 'stream_upload', filename), f'test/{filename}', timeout=60)
        except PathExistsError:
            print('File already exists')




# пока не требуется
async def ya_disk_remove(filename):
    token = os.getenv('YANDEX_TOKEN')
    client = yadisk.AsyncClient(token=token)
    # удаляет файл, если он существует надо добавить юид
    try:
        await client.remove(f"/test/{filename}", permanently=True)
        return {'status': 'removed successfully'}
    except PathNotFoundError:
        return {'status': 'does not exists'}