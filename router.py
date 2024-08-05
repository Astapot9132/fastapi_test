import asyncio
from fastapi import APIRouter, Depends, UploadFile, HTTPException, Request
from sqlalchemy.exc import IntegrityError
from starlette import status
from starlette.requests import ClientDisconnect
from streaming_form_data import StreamingFormDataParser
from streaming_form_data.targets import FileTarget, ValueTarget
from config import *
from repository import FileRepository
from schemas import SchemaFileAdd
from uuid import uuid4
from yandex_tools import ya_disk_upload



router = APIRouter(
    prefix='/files'
)

# обычная загрузка файла, тестил разницу в скорости
@router.post("/upload_file")
async def upload_file(file: UploadFile):
    print(file)
    with open(os.path.join(os.getcwd(), 'upload_files', file.filename), 'wb') as f:
        f.write(await file.read())
    return {'status': 'ok'}


# загрузка файла в потоке
@router.post('/stream_upload')
async def upload(request: Request):
    # так как при потоковой загрузке мы работаем с объектом запроса то все данные получаем из него
    filename = request.headers.get('filename')
    unique_id = str(uuid4())
    filename_with_uuid = f'{unique_id}_{os.path.basename(filename)}'
    file_ext = os.path.splitext(filename_with_uuid)[1]
    file_size = 0

    if not filename:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Filename header is missing')

    try:
        filepath = os.path.join('./', 'stream_upload', filename_with_uuid)
        file_to = FileTarget(filepath)
        data = ValueTarget()
        parser = StreamingFormDataParser(headers=request.headers)
        parser.register('file', file_to)
        parser.register('data', data)
        # как вариант получаем размер файла из чанков
        async for chunk in request.stream():
            file_size += len(chunk)
            parser.data_received(chunk)


    # некоторые ошибки которые могут возникнуть
    except ClientDisconnect:
        print('Client disconnect')
        return HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT,
                             detail='Reload connection')
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f'While uploading get an error: {e}')

    if not file_to.multipart_filename:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='File is missing')



    # отправляем в облачное хранилище (для тестов использовал яндекс диск)
    task1 = asyncio.create_task(ya_disk_upload(filename_with_uuid))


    # добавляем запись в БД
    file = {
        'filename': filename,
        'size': file_size,
        'extension': file_ext,
        'uuid': unique_id
    }
    try:
        file_in_schema = SchemaFileAdd(**file)
        task2 = asyncio.create_task(FileRepository.file_add(file_in_schema))
        await task2

    except IntegrityError:
        print('not unique uuid')

    await task1

    print(data.value.decode())
    print(file_to.multipart_filename)

    return {"message": f"Upload successful for {filename}"}









