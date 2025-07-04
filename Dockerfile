FROM python:3.12-slim

RUN apt update & mkdir /quiz

WORKDIR /quiz

COPY ./src ./src
COPY ./commands ./commands
COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip & pip install -r requirements.txt

CMD ["bash"]

# ["python", "src/manage.py", "runserver","0:8010"]
# docker build -t python_img .
# docker run --rm -it -d python_img
# docker run --rm -it -d --name python_cont python_img
# docker run --rm -it -d --name quiz_cont quiz_img