FROM python:3.8
WORKDIR /backend
RUN mkdir src
COPY . /src
RUN pip install -r requirements.txt
CMD ["python","-m", "src.app"]