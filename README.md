# Тестовое задание


1. Запрос отправляется на ручку /files/stream_upload
2. В headers - filename (название файла)
3. В files - file
4. В data - что угодно
5. Тестовые файлы класть в test_files

Реализована тестовая ручка /files/upload_files для проверки разницы в скорости

Для запуска проекта используйте docker-compose up --build

Проект доступен на порту 8002

Тестовый запрос в файле test.py

Для запуска необходимы следующие переменные:

 - YANDEX_TOKEN ( если хотите сохранить в облако )
 - POSTGRES_LOGIN 
 - POSTGRES_PASSWORD
 - POSTGRES_NAME 
 - POSTGRES_HOST=pgdb

