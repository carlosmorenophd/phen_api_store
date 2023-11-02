FROM python:3.9.18-bullseye
WORKDIR /app
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY app/ .

EXPOSE 8000
CMD ["python", "main.py"]