FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
VOLUME ./project
WORKDIR /fastapi_test
COPY requirements.txt /fastapi_test/
RUN pip install --no-cache-dir --upgrade -r /fastapi_test/requirements.txt
COPY . /fastapi_test
