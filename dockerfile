FROM python:3.11

WORKDIR /pw2

COPY . . 

ENTRYPOINT ["python", "__main__.py"]
