FROM python:3.12-slim

RUN apt update & mkdir /quiz

WORKDIR /quiz

COPY ./src ./src
COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip & pip install -r requirements.txt

CMD ["python", "src/manage.py", "runserver"]

# docker build -t python_img .
# docker run --rm -it -d python_img
# docker run --rm -it -d --name python_cont python_img
# docker run --rm -it -d --name quiz_cont quiz_img