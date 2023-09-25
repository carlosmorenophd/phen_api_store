FROM python:3.9.18-bullseye
WORKDIR /fastapi
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

copy app/ .

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]