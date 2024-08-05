import os
import httpx
import time

# Название файла для загрузки, тестовые файлы лежат в папке test_files
filename = "cat2.jpg"
# filename = 'cat_music.wav'
headers = {
    'Content-Type': 'application/json'

}

files = {'file': open(os.path.join(os.getcwd(), 'test_files', filename), 'rb')}
# body = {}
# start = time.time()
# response = requests.post('http://127.0.0.1:8000/files/upload_file', files=files)
# end = time.time()
# print(f'Затрачено: {end - start}s')
# print(response.json())



url ='http://127.0.0.1:8002/files/stream_upload'
files = {'file': open(os.path.join(os.getcwd(), 'test_files', filename), 'rb')}
headers = {'filename': filename}
data = {'data': 'Здесь могло быть ваше сообщение'}

with httpx.Client() as client:
    start = time.time()
    response = client.post(url, data=data, files=files, headers=headers, timeout=60)
    end = time.time()
    print(f'Затрачено: {end - start}s')
    print(response.status_code, response.json(), sep=' ')