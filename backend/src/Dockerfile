FROM python:3.8
WORKDIR /src
COPY . .
RUN pip install -r requirements.txt
ENV PORT=5000
EXPOSE 5000
CMD ["python", "app.py"]
