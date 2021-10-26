
FROM python:3.6.9

WORKDIR /project

COPY ./requirements.txt /project/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /project/requirements.txt

COPY ./src /project/src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
