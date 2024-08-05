# Тестовое задание
## Для запуска проекта используйте docker-compose up --build



1. Запрос отправляется на ручку /files/stream_upload
2. В headers - filename (название файла), в files - file, в data - что угодно
3. Если запустить через docker, файлы сохраняются в волюм fastapi
4. Если локально - файлы сохраняются в папку stream_upload
5. Тестовые файлы класть в test_files

Реализована тестовая ручка /files/upload_files для проверки разницы в скорости

Проект доступен на порту 8002

Тестовый запрос в файле test.py

Для запуска необходимы следующие переменные(указаны в config.py):

 - YANDEX_TOKEN ( если хотите сохранить в облако )
 - POSTGRES_LOGIN 
 - POSTGRES_PASSWORD
 - POSTGRES_NAME 
 - POSTGRES_HOST=pgdb

