FROM python:3.8
WORKDIR /backend
RUN mkdir src
COPY . /src
RUN pip install -r src/requirements.txt
CMD ["python","-m", "src.app"]