FROM python:3.10-slim

COPY . /src

COPY ./requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

EXPOSE 6060
ENV MY_ENV=netology
WORKDIR src

CMD ["python", "main.py", "--host", "0.0.0.0", "--port", "6060"]